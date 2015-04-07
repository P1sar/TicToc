

from PySide import QtGui,QtCore
import sys
from GameClient import GameClient
from NetGameDialog import NetGameDialog

class MyTable(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle("Server's list")
        self.setFixedSize(440,250)
        self.filled_rows = 0
        self.game_client = GameClient(self)

        self.tablewidget=QtGui.QTableWidget(1,4,self)
        self.tablewidget.setFixedSize(440,250)
        self.tablewidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        HeaderIp=QtGui.QTableWidgetItem("IP")
        HeaderRow=QtGui.QTableWidgetItem("Row")
        HeaderCol=QtGui.QTableWidgetItem("Col")
        HeaderConnect=QtGui.QTableWidgetItem("Win line")

        self.tablewidget.setHorizontalHeaderItem(0,HeaderIp)
        self.tablewidget.setHorizontalHeaderItem(1,HeaderRow)
        self.tablewidget.setHorizontalHeaderItem(2,HeaderCol)
        self.tablewidget.setHorizontalHeaderItem(3,HeaderConnect)

        cell_clicked = self.tablewidget.cellDoubleClicked
        cell_clicked.connect(self.server_choosed)

        self.game_client.writeMsg(["FindGame"])

    def fillTable(self, msg):
        print msg
        for game in msg:
            parse_game = game.split('|')

            ip = QtGui.QTableWidgetItem(parse_game[0])
            row = QtGui.QTableWidgetItem(parse_game[1])
            col = QtGui.QTableWidgetItem(parse_game[2])
            win_line = QtGui.QTableWidgetItem(parse_game[3])

            self.tablewidget.setItem(self.filled_rows, 0, ip)
            self.tablewidget.setItem(self.filled_rows, 1, row)
            self.tablewidget.setItem(self.filled_rows, 2, col)
            self.tablewidget.setItem(self.filled_rows, 3, win_line)

            self.filled_rows +=1
            self.tablewidget.setRowCount(self.tablewidget.rowCount()+1)

    def server_choosed(self, row, col):
        ip = self.tablewidget.item(row, 0).text()
        game_row = int(self.tablewidget.item(row, 1).text())
        game_col = int(self.tablewidget.item(row, 2).text())
        win_lane = int(self.tablewidget.item(row, 3).text())

        ngd = NetGameDialog(game_row,
                            game_col,
                            win_lane,
                            self,
                            self.game_client,
                            False,
                            ip)

        self.setHidden(True)
        ngd.exec_()
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    table = MyTable()
    table.show()
    sys.exit(app.exec_())