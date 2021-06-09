import sys
from time import sleep

import pygame

from TicTacToe import Const
from TicTacToe.model.Player import Player
from TicTacToe.view.ScreenMenager import GameState

pom_tab = [0, 1]


class Controller():
    def __init__(self, board, view):
        self.board = board
        self.view = view
        self.view.draw_lines()
        self.players = [Player(1), Player(2)]
        self.current_player = self.players[0]

    def check_events(self, event):
        mouse_up = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_up = True

        self.view.buttons.draw(self.view.screen)

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not self.board.game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // Const.SQUARE_SIZE)
            clicked_col = int(mouseX // Const.SQUARE_SIZE)
            if clicked_col > 2 or clicked_row > 2:
                pass
            else:
                if self.board.available_square(clicked_row, clicked_col):

                    self.board.mark_square(clicked_row, clicked_col, self.current_player.number)
                    if self.check_win(self.current_player):
                        self.board.game_over = True

                    self.swap_players()

                    self.view.draw_figures(self.board.get_matrix())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.current_player.number = 1
                self.board.game_over = False

        for button in self.view.buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            if self.board.game_over == True:

                for i in pom_tab:
                    if i == 0:
                        pom_tab.remove(0)
                        break
                    sleep(2)
                    pom_tab.insert(0, 0)
                    return GameState.TITLE

    def swap_players(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def restart(self):
        self.view.screen.fill(Const.BG_COLOR)
        self.view.draw_lines()
        for row in range(Const.BOARD_ROWS):
            for col in range(Const.BOARD_COLS):
                self.board.matrix[row][col] = 0

    def check_win(self, player):
        # vertical win check
        for col in range(Const.BOARD_COLS):
            if self.board.matrix[0][col] == player.number and self.board.matrix[1][col] == player.number and \
                    self.board.matrix[2][
                        col] == player.number:
                self.view.draw_vertical_winning_line(col, player)
                return True

        # horizontal win check
        for row in range(Const.BOARD_ROWS):
            if self.board.matrix[row][0] == player.number and self.board.matrix[row][1] == player.number and \
                    self.board.matrix[row][
                        2] == player.number:
                self.view.draw_horizontal_winning_line(row, player)
                return True

        # asc diagonal win check
        if self.board.matrix[2][0] == player.number and self.board.matrix[1][1] == player.number and self.board.matrix[0][
            2] == player.number:
            self.view.draw_asc_diagonal(player)
            return True

        # desc diagonal win chek
        if self.board.matrix[0][0] == player.number and self.board.matrix[1][1] == player.number and self.board.matrix[2][
            2] == player.number:
            self.view.draw_desc_diagonal(player)
            return True

        if self.board.is_board_full():
            return True

        return False
