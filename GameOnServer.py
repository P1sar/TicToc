#from ServerSocket import ServerSocket
import random

class GameOnServer():
    def __init__(self, rows, cols, win_lane, creator):
        self.rows = rows
        self.cols = cols
        self.win_lane = win_lane
        self.cretator = creator
        self.second_player = None

    def connectNewPlayer(self, second_player):
        self.second_player = second_player
        self.second_player.current_game = self

        if random.randrange(0, 2):
            msg = ["Message", "Your turn!", "X"]
            self.cretator.writeMsg(msg)
        else:
            msg = ["Message", "Your turn!", "O"]
            self.second_player.writeMsg(msg)

    def newTurn(self, who_turned, msg):
        if who_turned is self.cretator:
            self.second_player.writeMsg(msg)
        else:
            self.cretator.writeMsg(msg)


