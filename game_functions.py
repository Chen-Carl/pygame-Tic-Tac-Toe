import sys
import pygame

from chessboard import Chessboard
from piece import Piece


def check_events(screen, chessboard, pieces, ai_settings, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_piece(screen, chessboard, mouse_x, mouse_y, pieces, ai_settings, stats)

def update_screen(ai_settings, screen, chessboard, pieces):
    screen.fill(ai_settings.bg_color)
    chessboard.blit_board()
    for piece in pieces.sprites():
        piece.blit_piece()

    pygame.display.flip()

def new_piece(screen, chessboard, mouse_x, mouse_y, pieces, ai_settings, stats):
    
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
        
        piece = Piece(screen, rect_x, rect_y, ai_settings)
        pieces.add(piece)
        if ai_settings.piece_choose == 1:
            ai_settings.piece_choose = 0
            chessboard.boxes_status[index] = 2
        elif ai_settings.piece_choose == 0:
            ai_settings.piece_choose = 1
            chessboard.boxes_status[index] = 1
        judge_winner(chessboard, stats)

    elif i >= 0 and j >= 0 and chessboard.boxes_status[index] == 1:
        pass
    elif index < 0:
        pass
    
def judge_winner(chessboard, stats):
    win1 = chessboard.boxes_status[0] == chessboard.boxes_status[1] and chessboard.boxes_status[1] == chessboard.boxes_status[2] and chessboard.boxes_status[0] != 0
    win2 = chessboard.boxes_status[3] == chessboard.boxes_status[4] and chessboard.boxes_status[4] == chessboard.boxes_status[5] and chessboard.boxes_status[3] != 0
    win3 = chessboard.boxes_status[6] == chessboard.boxes_status[7] and chessboard.boxes_status[7] == chessboard.boxes_status[8] and chessboard.boxes_status[6] != 0
    win4 = chessboard.boxes_status[0] == chessboard.boxes_status[3] and chessboard.boxes_status[3] == chessboard.boxes_status[6] and chessboard.boxes_status[0] != 0
    win5 = chessboard.boxes_status[1] == chessboard.boxes_status[4] and chessboard.boxes_status[4] == chessboard.boxes_status[7] and chessboard.boxes_status[1] != 0
    win6 = chessboard.boxes_status[2] == chessboard.boxes_status[5] and chessboard.boxes_status[5] == chessboard.boxes_status[8] and chessboard.boxes_status[2] != 0
    win7 = chessboard.boxes_status[0] == chessboard.boxes_status[4] and chessboard.boxes_status[4] == chessboard.boxes_status[8] and chessboard.boxes_status[0] != 0
    win8 = chessboard.boxes_status[2] == chessboard.boxes_status[4] and chessboard.boxes_status[4] == chessboard.boxes_status[6] and chessboard.boxes_status[2] != 0
    win = [win1, win2, win3, win4, win5, win6, win7, win8]
    for i in range(8):
        if win[i]:
            print("Winner: 1")
            stats.game_active = False
