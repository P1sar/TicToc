from PySide import QtGui, QtCore
from GameDialog import GameDialog
from NetGameDialog import NetGameDialog
import sys

class CreateGame(QtGui.QDialog):
    def __init__(self, net=False, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.is_net = net

        main_hbox = QtGui.QHBoxLayout()
        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()

        self.setWindowTitle("Create the game")
        self.setFixedSize(300,250)
        self.setWindowIcon(QtGui.QIcon("icons/TIC_TAK.png"))
        self.setStyleSheet("background-color: rgb(255,228,181)")

        #LABELS
        game_rulez_label=QtGui.QLabel(self)
        game_rulez_label.setAlignment(QtCore.Qt.AlignCenter)
        game_rulez_label.setText("Create Game")
        game_rulez_label.setStyleSheet("QLabel{font:18pt;font-weight:bold}")
        game_rulez_label.setFixedSize(200,25)

        height_spin_label=QtGui.QLabel(self)
        height_spin_label.setAlignment(QtCore.Qt.AlignCenter)
        height_spin_label.setText("Desk height")
        height_spin_label.setStyleSheet("QLabel{font:10pt;}")
        height_spin_label.setFixedSize(100,25)

        width_spin_label=QtGui.QLabel(self)
        width_spin_label.setAlignment(QtCore.Qt.AlignCenter)
        width_spin_label.setText("Desk width")
        width_spin_label.setStyleSheet("QLabel{font:10pt;}")
        width_spin_label.setFixedSize(100,25)

        win_lane_spin_label=QtGui.QLabel(self)
        win_lane_spin_label.setAlignment(QtCore.Qt.AlignCenter)
        win_lane_spin_label.setText("WIN LANE!")
        win_lane_spin_label.setStyleSheet("QLabel{font:10pt;}")
        win_lane_spin_label.setFixedSize(100,25)

        #SPIN_BOXES PARAMETRES
        self.height_spin=QtGui.QSpinBox(self)
        self.height_spin.setMinimum(3)
        self.height_spin.setMaximum(25)
        self.height_spin.setFixedSize(100,25)
        self.height_spin.setStyleSheet("background-color:white")
        self.height_spin.valueChanged.connect(self.sizeSpinChanged)

        self.width_spin=QtGui.QSpinBox(self)
        self.width_spin.setMinimum(3)
        self.width_spin.setMaximum(25)
        self.width_spin.setFixedSize(100,25)
        self.width_spin.setStyleSheet("background-color:white")
        self.width_spin.valueChanged.connect(self.sizeSpinChanged)

        self.win_lane=QtGui.QSpinBox(self)
        self.win_lane.setMinimum(3)
        self.win_lane.setMaximum(25)
        self.win_lane.setFixedSize(100,25)
        self.win_lane.setStyleSheet("background-color:white")
        self.win_lane.valueChanged.connect(self.sizeSpinChanged)

        #START GAME BUTTON

        start_game_button=QtGui.QPushButton("Accept settings",self)
        start_game_button.setFixedSize(100,45)
        start_game_button.setStyleSheet("background-color: rgb(205,133,63)")
        start_game_button.clicked.connect(self.startGame)

        vbox.addWidget(game_rulez_label)

        hbox.addWidget(height_spin_label)
        hbox.addWidget(self.height_spin)
        vbox.addLayout(hbox)
        hbox = QtGui.QHBoxLayout()

        hbox.addWidget(width_spin_label)
        hbox.addWidget(self.width_spin)
        vbox.addLayout(hbox)
        hbox = QtGui.QHBoxLayout()

        hbox.addWidget(win_lane_spin_label)
        hbox.addWidget(self.win_lane)
        vbox.addLayout(hbox)
        hbox = QtGui.QHBoxLayout()

        hbox.addWidget(start_game_button)
        vbox.addLayout(hbox)
        hbox = QtGui.QHBoxLayout()

        main_hbox.addLayout(vbox)
        self.setLayout(main_hbox)

    def startGame(self):
        rows = self.height_spin.value()
        cols = self.width_spin.value()
        win_lane = self.win_lane.value()
        gd = None

        if self.is_net:
            gd = NetGameDialog(rows, cols, win_lane, self)
        else:
            gd = GameDialog(rows, cols, win_lane, self)

        self.setHidden(True)
        gd.exec_()
        self.close()


    def sizeSpinChanged(self, value):
        height = self.height_spin.value()
        width = self.width_spin.value()
        win_lane = self.win_lane.value()

        if win_lane > height and win_lane > width:
            if not self.win_lane is self.sender():
                self.win_lane.setValue(value)
            else:
                self.win_lane.setValue(height)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	cg=CreateGame()
	cg.show()
	sys.exit(app.exec_())
