from PySide import QtCore, QtNetwork
from BaseSocket import BaseSocket
from GameOnServer import GameOnServer

class ServerSocket(BaseSocket):
    def __init__(self, my_sock, server):
        BaseSocket.__init__(self, my_sock)
        self.current_game = None
        self.server = server

    def msgParser(self, msg):
        command = msg[0]

        if command == "CreateGame":
            self.current_game = GameOnServer(msg[1], msg[2], msg[3], self)
            print "Create Game"
        elif command == "ConnectToGame":
            IP = msg[1]
            creator = None

            for i in self.server.clients:
                if i.my_sock.peerAddress().toString() == IP:
                    creator = i
                    break

            creator.current_game.connectNewPlayer(self)
        elif command == "NewTurn":
            self.current_game.newTurn(self, msg)
        elif command == "FindGame":
            msg = ["FindedGame"]
            for client in self.server.clients:
                game = client.current_game
                if game != None and game.second_player == None:
                    game_to_msg = [str(client.my_sock.peerAddress().toString()), str(game.rows), str(game.cols), str(game.win_lane)]
                    game_to_msg = '|'.join(game_to_msg)
                    msg.append(game_to_msg)

            self.writeMsg(msg)







