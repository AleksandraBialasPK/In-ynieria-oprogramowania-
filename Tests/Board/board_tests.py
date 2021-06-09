import unittest

import numpy as np
import pygame

from TicTacToe.controller.Controller import Controller
from TicTacToe.model.Board import Board
from TicTacToe.model.Player import Player
from TicTacToe.view.View import View

pygame.init()


class WinTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.view = View()
        self.controller = Controller(self.board, self.view)
        self.player = Player(1)

    def test_checks_win_in_first_row(self):
        #Given
        self.board = Board()
        self.view = View()
        self.controller = Controller(self.board, self.view)
        self.player = Player(1)
        # When
        self.board.matrix[0][0] = 1
        self.board.matrix[0][1] = 1
        self.board.matrix[0][2] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)
        self.board.matrix = np.zeros(([3, 3]))

    def test_checks_win_in_second_row(self):
        # When
        self.board.matrix[1][0] = 1
        self.board.matrix[1][1] = 1
        self.board.matrix[1][2] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_win_in_third_row(self):
        # When
        self.board.matrix[2][0] = 1
        self.board.matrix[2][1] = 1
        self.board.matrix[2][2] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_win_in_first_column(self):
        # When
        self.board.matrix[0][0] = 1
        self.board.matrix[1][0] = 1
        self.board.matrix[2][0] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_win_in_second_column(self):
        # When
        self.board.matrix[0][1] = 1
        self.board.matrix[1][1] = 1
        self.board.matrix[2][1] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_win_in_third_column(self):
        # When
        self.board.matrix[0][2] = 1
        self.board.matrix[1][2] = 1
        self.board.matrix[2][2] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_win_in_asc_diagonal(self):
        # When
        self.board.matrix[0][2] = 1
        self.board.matrix[1][1] = 1
        self.board.matrix[2][0] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_win_in_dsc_diagonal(self):
        # When
        self.board.matrix[0][0] = 1
        self.board.matrix[1][1] = 1
        self.board.matrix[2][2] = 1
        # Then
        result = self.controller.check_win(self.player)
        self.assertTrue(result)

    def test_checks_tie(self):
        # When
        self.board.matrix.fill(1)
        # Then
        result = self.board.is_board_full()
        self.assertTrue(result)

    def test_check_if_board_is_empty(self):
        #Given
        self.board.matrix.fill(0)
        # Then
        for row in range(0, 3):
            for col in range(0, 3):
                result = self.board.available_square(row, col)
                self.assertTrue(result)

    def test_check_if_board_is_not_empty(self):
        #When
        self.board.matrix[0][1] = 1
        #Then
        result = self.board.available_square(0, 1)
        self.assertFalse(result)

    def test_check_if_board_is_full(self):
        # When
        self.board.matrix.fill(1)
        for row in range(0, 3):
            for col in range(0, 3):
                self.board.matrix[row][col] = 1
        # Then
        result = self.board.is_board_full()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
