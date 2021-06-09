import numpy

from TicTacToe import Const


class Board():
    def __init__(self):
        self.matrix = numpy.zeros((Const.BOARD_ROWS, Const.BOARD_COLS))
        self.game_over = False

    def mark_square(self, row, col, player):
        if row >= 3 or col >= 3:
            pass
        else:
            self.matrix[row][col] = player

    def available_square(self, row, col):
        return self.matrix[row][col] == 0

    def is_board_full(self):
        for row in range(Const.BOARD_ROWS):
            for col in range(Const.BOARD_COLS):
                if self.matrix[row][col] == 0:
                    return False

        return True

    def get_matrix(self):
        return self.matrix

