from PySide import QtGui,QtCore
from CreateGame import CreateGame
import sys
from connectionTable import MyTable

class StartWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()

        self.setWindowTitle("TIC! TAK! TOE!")
        self.setWindowIcon(QtGui.QIcon("icons/TIC_TAK.png"))
        self.setStyleSheet("background-color: rgb(255,228,181)")
        self.setFixedSize(300, 500)

        self.create_game = QtGui.QPushButton("Create Game",self)
        self.create_game.setFixedSize(125,125)
        self.create_game.setStyleSheet(" background-color: rgb(205,133,63) ")
        self.create_game.clicked.connect(self.nextWindow)

        self.create_net_game = QtGui.QPushButton("Create network Game",self)
        self.create_net_game.setFixedSize(125,125)
        self.create_net_game.setStyleSheet(" background-color: rgb(205,133,63) ")
        self.create_net_game.clicked.connect(self.nextWindow)

        find_game=QtGui.QPushButton("Find Game",self)
        find_game.setFixedSize(125,125)
        find_game.setStyleSheet(" background-color: rgb(205,133,63) ")
        find_game.clicked.connect(self.findGame)

        vbox.addWidget(self.create_game)
        vbox.addWidget(self.create_net_game)
        vbox.addWidget(find_game)

        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def findGame(self):
        findGameDialog = MyTable(self)

        self.setHidden(True)

        findGameDialog.exec_()

        self.setVisible(True)

    def nextWindow(self):
        cg = None

        if self.sender() is self.create_game:
            cg = CreateGame(False, self)
        else:
            cg = CreateGame(True, self)

        self.setHidden(True)

        cg.exec_()

        self.setVisible(True)

    def startwindow_center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    mainWindow=StartWindow()
    mainWindow.show()
    sys.exit(app.exec_())