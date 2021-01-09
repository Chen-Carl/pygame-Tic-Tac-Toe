import sys
import pygame

import game_functions as gf
from settings import Settings
from chessboard import Chessboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Tic-Tac-Toe")

    chessboard = Chessboard(screen)

    # event loop
    while True:
        # listening events from mouse and keyboard
        gf.check_events()

        # visualize
        gf.update_screen(ai_settings, screen, chessboard)

run_game()