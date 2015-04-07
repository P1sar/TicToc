import os


class GameDesk():
    def __init__(self, rows, cols, win_line):
        self.win_line = win_line
        self.desk = []
        self.rows = rows# + 2
        self.cols = cols# + 2

        for row in range(0, self.rows):
            inner_desk = []

            for col in range(0, self.cols):
                inner_desk.append('_')

            self.desk.append(inner_desk)

    def clearDesk(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.desk[row][col] = '_'

    def showDesk(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols - 1):
                print self.desk[row][col],
            print self.desk[row][self.cols-1]

    def newTurn(self, row, col, char):
        self.desk[row][col] = char

        return self.isEnded(row, col, char)

    def lineCounter(self, row, col, char, rise_x, rise_y):
        counter = 0

        y = row + rise_y
        x = col + rise_x

        while y >= 0 and x >= 0 and y < self.rows and x < self.cols:
            if self.desk[y][x] == char:
                counter += 1
            else:
                return counter

            x += rise_x
            y += rise_y

        return counter

    def isEnded(self, row, col, char):
        result = False

        top_left_line = self.lineCounter(row, col, char, -1, -1)
        top_line = self.lineCounter(row, col, char, 0, -1)
        top_right_line = self.lineCounter(row, col, char, 1, -1)
        right_line = self.lineCounter(row, col, char, 1, 0)
        down_right_line = self.lineCounter(row, col, char, 1, 1)
        down_line = self.lineCounter(row, col, char, 0, 1)
        down_left_line = self.lineCounter(row, col, char, -1, 1)
        left_line = self.lineCounter(row, col, char, -1, 0)

        if top_left_line + down_right_line + 1 >= self.win_line:
            result = True
        elif top_line + down_line + 1 >= self.win_line:
            result = True
        elif top_right_line + down_left_line + 1 >= self.win_line:
            result = True
        elif left_line + right_line + 1 >= self.win_line:
            result = True

        return result

    def convertToStringList(self):
        desk_string_list = []

        for row in range(0, self.rows):
            desk_string = '|'.join(self.desk[row])
            desk_string_list.append(desk_string)

        return desk_string_list


    def convertToListList(self, desk_string_list):
        desk_list = []
        desk_list_list = []

        for list in self.desk_string_list:
            desk_list = list.split('|')
            desk_list_list.append(desk_list)

        self.desk = desk_list_list



if __name__ == "__main__":
    game = GameDesk(7, 5, 3)

    end = False
    char = 'X'
    while not end:
        cord_x = input("cord x: ")
        cord_y = input("cord y: ")

        os.system("cls")

        end = game.newTurn(cord_y, cord_x, char)
        game.showDesk()

        if end:
            print "Won " + char

        if char == 'X':
            char = '0'
        else:
            char = 'X'
