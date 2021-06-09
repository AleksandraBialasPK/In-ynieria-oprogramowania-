import pygame
from pygame.sprite import RenderUpdates

from TicTacToe import Const
from TicTacToe.view.ScreenMenager import Button, GameState


class View():
    def __init__(self):
        self.screen = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        self.screen.fill(Const.BACKGROUND_COLOR)
        pygame.display.set_caption('TIC TAC TOE')

        self.return_btn = Button(
            center_position=(200, 500),
            font_size=30,
            bg_rgb=Const.BACKGROUND_COLOR,
            text_rgb=Const.FONT_COLOR,
            text="End Game",
            action=GameState.TITLE,
        )

        self.buttons = RenderUpdates(self.return_btn)

    def draw_lines(self):
        # 1 horizontal
        pygame.draw.line(self.screen, Const.LINE_COLOR, (0, Const.SQUARE_SIZE),
                         (3 * Const.SQUARE_SIZE, Const.SQUARE_SIZE),
                         Const.LINE_WIDTH)
        # 2 horizontal
        pygame.draw.line(self.screen, Const.LINE_COLOR, (0, 2 * Const.SQUARE_SIZE),
                         (3 * Const.SQUARE_SIZE, 2 * Const.SQUARE_SIZE), Const.LINE_WIDTH)

        # 1 vertical
        pygame.draw.line(self.screen, Const.LINE_COLOR, (Const.SQUARE_SIZE, 0),
                         (Const.SQUARE_SIZE, 3 * Const.SQUARE_SIZE),
                         Const.LINE_WIDTH)
        # 2 vertical
        pygame.draw.line(self.screen, Const.LINE_COLOR, (2 * Const.SQUARE_SIZE, 0),
                         (2 * Const.SQUARE_SIZE, 3 * Const.SQUARE_SIZE), Const.LINE_WIDTH)

    def draw_figures(self, matrix):
        for row in range(Const.BOARD_ROWS):
            for col in range(Const.BOARD_COLS):
                if matrix[row][col] == 1:
                    pygame.draw.circle(self.screen, Const.CIRCLE_COLOR, (
                        int(col * Const.SQUARE_SIZE + Const.SQUARE_SIZE // 2),
                        int(row * Const.SQUARE_SIZE + Const.SQUARE_SIZE // 2)), Const.CIRCLE_RADIUS,
                                       Const.CIRCLE_WIDTH)
                elif matrix[row][col] == 2:
                    pygame.draw.line(self.screen, Const.CROSS_COLOR,
                                     (col * Const.SQUARE_SIZE + Const.SPACE,
                                      row * Const.SQUARE_SIZE + Const.SQUARE_SIZE - Const.SPACE),
                                     (col * Const.SQUARE_SIZE + Const.SQUARE_SIZE - Const.SPACE,
                                      row * Const.SQUARE_SIZE + Const.SPACE), Const.CROSS_WIDTH)
                    pygame.draw.line(self.screen, Const.CROSS_COLOR,
                                     (col * Const.SQUARE_SIZE + Const.SPACE, row * Const.SQUARE_SIZE + Const.SPACE),
                                     (col * Const.SQUARE_SIZE + Const.SQUARE_SIZE - Const.SPACE,
                                      row * Const.SQUARE_SIZE + Const.SQUARE_SIZE - Const.SPACE), Const.CROSS_WIDTH)

    def draw_vertical_winning_line(self, col, player):
        posX = col * Const.SQUARE_SIZE + Const.SQUARE_SIZE // 2

        if player.number == 1:
            color = Const.CIRCLE_COLOR
        elif player.number == 2:
            color = Const.CROSS_COLOR

        pygame.draw.line(self.screen, color, (posX, 15), (posX, 3 * Const.SQUARE_SIZE), Const.LINE_WIDTH)

    def draw_horizontal_winning_line(self, row, player):
        posY = row * Const.SQUARE_SIZE + Const.SQUARE_SIZE // 2

        if player.number == 1:
            color = Const.CIRCLE_COLOR
        elif player.number == 2:
            color = Const.CROSS_COLOR

        pygame.draw.line(self.screen, color, (15, posY), (3 * Const.SQUARE_SIZE, posY), Const.WIN_LINE_WIDTH)

    def draw_asc_diagonal(self, player):
        if player.number == 1:
            color = Const.CIRCLE_COLOR
        elif player.number == 2:
            color = Const.CROSS_COLOR

        pygame.draw.line(self.screen, color, (5, 3 * Const.SQUARE_SIZE), (3 * Const.SQUARE_SIZE, 5),
                         Const.WIN_LINE_WIDTH)

    def draw_desc_diagonal(self, player):
        if player.number == 1:
            color = Const.CIRCLE_COLOR
        elif player.number == 2:
            color = Const.CROSS_COLOR

        pygame.draw.line(self.screen, color, (15, 15), (3 * Const.SQUARE_SIZE, 3 * Const.SQUARE_SIZE),
                         Const.WIN_LINE_WIDTH)
