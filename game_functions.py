import sys
import pygame

from chessboard import Chessboard
from piece import Piece


def check_events(screen, chessboard, pieces):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_piece(screen, chessboard, mouse_x, mouse_y, pieces)

def update_screen(ai_settings, screen, chessboard, pieces):
    screen.fill(ai_settings.bg_color)
    chessboard.blit_board()
    for piece in pieces.sprites():
        piece.blit_piece()
    pygame.display.flip()

def new_piece(screen, chessboard, mouse_x, mouse_y, pieces):
    
    if mouse_x > 50 and mouse_x < 50 + 195:
        i = 0
    elif mouse_x > 250 and mouse_x < 250 + 195:
        i = 1
    elif mouse_x > 450 and mouse_x < 450 + 195:
        i = 2
    else:
        i = -1
    
    if mouse_y > 50 and mouse_y < 50 + 195:
        j = 0
    elif mouse_y > 250 and mouse_y < 250 + 195:
        j = 1
    elif mouse_y > 450 and mouse_y < 450 + 195:
        j = 2
    else:
        j = -1

    index = i * 3 + j
    if index >= 0 and chessboard.boxes_status[index] == 0:
        # get the position to place a new piece
        rect_x = chessboard.boxes[index][0] + 97
        rect_y = chessboard.boxes[index][1] + 192
        print(rect_x, rect_y)
        chessboard.boxes_status[index] = 1
        piece = Piece(screen, rect_x, rect_y)
        pieces.add(piece)

    elif index >= 0 and chessboard.boxes_status[index] == 1:
        pass
    elif index < 0:
        pass
    