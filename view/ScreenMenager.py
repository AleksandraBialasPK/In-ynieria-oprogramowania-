from enum import Enum

import pygame
import pygame.freetype
from pygame.sprite import RenderUpdates
from pygame.sprite import Sprite

from TicTacToe import Const


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """Return: surface with text written on, converted"""
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class Button(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            from TicTacToe.GameMenager import game_manager
            game_state = game_manager()
            game_state = GameState.TITLE

        if game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen):
    start_btn = Button(
        center_position=(200, 250),
        font_size=30,
        bg_rgb=Const.BACKGROUND_COLOR,
        text_rgb=Const.FONT_COLOR,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = Button(
        center_position=(200, 350),
        font_size=30,
        bg_rgb=Const.BACKGROUND_COLOR,
        text_rgb=Const.FONT_COLOR,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn, quit_btn)

    return game_loop(screen, buttons)


def start_new_game(screen):
    return_btn = Button(
        center_position=(300, 550),
        font_size=20,
        bg_rgb=Const.BACKGROUND_COLOR,
        text_rgb=Const.FONT_COLOR,
        text="End Game",
        action=GameState.TITLE,
    )

    buttons = RenderUpdates(return_btn)

    return game_loop(screen, buttons)


def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:

        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(Const.BACKGROUND_COLOR)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)

            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


if __name__ == "__main__":
    main()
