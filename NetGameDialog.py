from PySide import QtGui, QtCore
import sys
import random
from GameDesk import GameDesk
from GameButton import GameButton
from GameClient import GameClient


class NetGameDialog(QtGui.QDialog):
    def __init__(self, rows, cols, win_lane, parent=None, sock=None, create=True, IP=""):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle("The Network Game")
        self.buttons = []
        self.char = ""
        self.game_client = None
        if sock == None:
            self.game_client = GameClient(self)
        else:
            self.game_client = sock
            self.game_client.dialog = self

        self.game_desk = GameDesk(rows, cols, win_lane)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(0)

        for row in range(0, rows):
            for col in range(0, cols):
                button = GameButton(row, col)
                button.setEnabled(False)
                button.clicked.connect(self.gameButtonClicked)
                self.buttons.append(button)
                self.grid.addWidget(button, row, col)

        self.setLayout(self.grid)

        if create:
            msg = ["CreateGame", str(rows), str(cols), str(win_lane)]
            self.game_client.writeMsg(msg)
        else:
            msg = ["ConnectToGame", IP]
            self.game_client.writeMsg(msg)

    def myTurn(self, char):
        self.char = char

        for b in self.buttons:
            b.setEnabled(True)
        reply = QtGui.QMessageBox.information(self, "Message", "Your turn!", QtGui.QMessageBox.Yes)

    def gameButtonClicked(self):
        for b in self.buttons:
            b.setEnabled(False)

        sender = self.sender()
        x = sender.pos_x
        y = sender.pos_y

        self.makeTurn(x, y, self.char, sender, True)

        msg = ["NewTurn", str(x), str(y), self.char]
        self.game_client.writeMsg(msg)

    def makeTurn(self, x, y, char, button=None, my_turn=False):
        x=int(x)
        y=int(y)
        if button == None:
            for b in self.buttons:
                #print b.pos_x,b.pos_y
                #print x,y
                if int(b.pos_x) == int(x) and int(b.pos_y) == int(y):
                    button = b


        label = QtGui.QLabel(char)
        label.setFixedSize(25, 25)
        label.setAlignment(QtCore.Qt.AlignCenter)

        if char == "X":
            label.setStyleSheet("QLabel{color: green}")
        else:
            label.setStyleSheet("QLabel{color: red}")
        font = label.font()
        font.setPointSize(20)
        font.setBold(True)

        label.setFont(font)
        button.close()
        self.grid.addWidget(label, x, y, QtCore.Qt.AlignCenter)

        if self.game_desk.newTurn(x, y, char):
            reply = QtGui.QMessageBox.information(self, "Message", (char + " WON!"), QtGui.QMessageBox.Yes)
            #self.game_client.my_sock.disconnect()

            self.close()

        if not my_turn:
            if char == "X":
                self.myTurn("O")
            else:
                self.myTurn("X")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gd = NetGameDialog(5, 7, 7)
    gd.show()
    sys.exit(app.exec_())