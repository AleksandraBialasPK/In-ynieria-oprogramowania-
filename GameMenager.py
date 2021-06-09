def game_manager():
    # MODULES
    import pygame
    from TicTacToe.controller.Controller import Controller
    from TicTacToe.model.Board import Board
    from TicTacToe.view.View import View

    # initializes pygame

    # --------
    # MAINLOOP
    # --------
    board = Board()
    view = View()
    controller = Controller(board, view)

    while True:
        for event in pygame.event.get():
            nav_value = controller.check_events(event)
            if nav_value is not None:
                return nav_value

        pygame.display.update()
