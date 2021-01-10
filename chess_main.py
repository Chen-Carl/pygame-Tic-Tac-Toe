import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from chessboard import Chessboard
from piece import Piece
from Game_stats import GameStats
from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(ai_settings, screen, "Play")
    pygame.display.set_caption("Tic-Tac-Toe")

    chessboard = Chessboard(screen)
    stats = GameStats(ai_settings)
    pieces = Group()

    # event loop
    while True:
        # listening events from mouse and keyboard
        gf.check_events(chessboard.screen, chessboard, pieces, ai_settings, stats, play_button)
        # visualize
        if stats.game_active:
            gf.update_pieces(pieces, screen, chessboard, stats, ai_settings)
        gf.update_screen(ai_settings, screen, chessboard, pieces, play_button, stats)


run_game()