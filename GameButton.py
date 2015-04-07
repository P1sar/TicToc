from PySide import QtGui, QtCore

class GameButton(QtGui.QPushButton):
	def __init__ (self, x, y, parent=None):
		QtGui.QPushButton.__init__(self, parent)
		self.pos_x = x
		self.pos_y = y
		self.setFixedSize(25, 25)