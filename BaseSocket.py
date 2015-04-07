from PySide import QtCore, QtNetwork

SIZEOF_UINT32 = 4

class BaseSocket(QtCore.QObject):
    def __init__(self, serv_sock = None):
        QtCore.QObject.__init__(self)
        if serv_sock == None:
            self.my_sock = QtNetwork.QTcpSocket(self)
        else:
            self.my_sock = serv_sock

        self.my_sock.readyRead.connect(self.readMsg)
        self.my_sock.disconnected.connect(self.on_disconnected)

        self.signal_disconnected = QtCore.Signal()

        self.nextBlockSize = 0

    def readMsg(self):
        in_stream = QtCore.QDataStream(self.my_sock)
        in_stream.setVersion(QtCore.QDataStream.Qt_4_8)
        msg = []

        while True:
            if self.nextBlockSize == 0:
                if self.my_sock.bytesAvailable() < SIZEOF_UINT32:
                    return
                self.nextBlockSize = in_stream.readUInt32()
            if self.my_sock.bytesAvailable() < self.nextBlockSize:
                return

            msg = in_stream.readQStringList()
            self.nextBlockSize = 0
            self.msgParser(msg)

    def msgParser(self, msg):
        pass

    def writeMsg(self, msg):
        request = QtCore.QByteArray()
        out_stream = QtCore.QDataStream(request, QtCore.QIODevice.WriteOnly)
        out_stream.setVersion(QtCore.QDataStream.Qt_4_8)
        out_stream.writeUInt32(0)
        out_stream.writeQStringList(msg)
        out_stream.device().seek(0)
        out_stream.writeUInt32(request.size() - SIZEOF_UINT32)
        self.my_sock.write(request)

    def on_disconnected(self):
        self.my_sock.deleteLater()
        #self.signal_disconnected.emit()