from PySide import QtCore, QtNetwork
from ServerSocket import ServerSocket
import sys

PORT = 9999

class GameServer(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

        self.server = QtNetwork.QTcpServer(self)
        self.server.listen(QtNetwork.QHostAddress.Any, PORT)
        self.server.newConnection.connect(self.addConnection)

        self.clients = []

    def addConnection(self):
        clientConnection = ServerSocket(self.server.nextPendingConnection(), self)
        self.clients.append(clientConnection)

        clientConnection.my_sock.disconnected.connect(self.on_disconnected)

    def on_disconnected(self):
        disconnected_socket = self.sender()
        self.clients.remove(disconnected_socket)


if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    s = GameServer()
    sys.exit(app.exec_())