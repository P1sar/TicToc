from PySide import QtGui, QtCore
import sys
import random
from GameDesk import GameDesk
from GameButton import GameButton
from Gamer import Gamer


class GameDialog(QtGui.QDialog):
    def __init__(self, rows, cols, win_lane, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.gamers_list = []

        for i in ["X", "O"]:
            self.gamer = Gamer()
            self.gamer.setView(i)
            self.gamers_list.append(self.gamer)

        random.seed()

        self.gamer_number = random.randrange(0, len(self.gamers_list))
        self.gamer = self.gamers_list[self.gamer_number].getView()

        self.setWindowTitle("The Game")

        self.game_desk = GameDesk(rows, cols, win_lane)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(0)

        for row in range(0, rows):
            for col in range(0, cols):
                button = GameButton(row, col)
                button.clicked.connect(self.gameButtonClicked)
                self.grid.addWidget(button, row, col)

        self.setLayout(self.grid)

    def gameButtonClicked(self):
        sender = self.sender()
        x = sender.pos_x
        y = sender.pos_y

        label = QtGui.QLabel(self.gamer)
        label.setFixedSize(25, 25)
        label.setAlignment(QtCore.Qt.AlignCenter)

        if self.gamer == "X":
            label.setStyleSheet("QLabel{color: green}")
        else:
            label.setStyleSheet("QLabel{color: red}")
        font = label.font()
        font.setPointSize(20)
        font.setBold(True)

        label.setFont(font)
        sender.close()
        self.grid.addWidget(label, x, y, QtCore.Qt.AlignCenter)

        if self.game_desk.newTurn(x, y, self.gamer):
            reply = QtGui.QMessageBox.information(self, "Message", (self.gamer + " WON!"), QtGui.QMessageBox.Yes)

            self.close()

        self.game_desk.showDesk()

        self.nextPlayer()

    def nextPlayer(self):
        if self.gamer_number == len(self.gamers_list) - 1:
            self.gamer_number = 0
        else:
            self.gamer_number += 1

        self.gamer = self.gamers_list[self.gamer_number].getView()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gd = GameDialog(5, 7, 7)
    gd.show()
    sys.exit(app.exec_())