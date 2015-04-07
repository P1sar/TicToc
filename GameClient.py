from PySide import QtCore, QtNetwork
from BaseSocket import BaseSocket

PORT = 9999

class GameClient(BaseSocket):
    def __init__(self, dialog):
        BaseSocket.__init__(self)

        self.my_sock.connectToHost("172.10.1.139", PORT)

        self.dialog = dialog

    def msgParser(self, msg):
        command = msg[0]

        if command == "Message":
            if msg[1] == "Your turn!":
                self.dialog.myTurn(msg[2])

        elif command == "NewTurn":
            self.dialog.makeTurn(msg[1], msg[2], msg[3])

        elif command == "FindedGame":
            self.dialog.fillTable(msg[1:])