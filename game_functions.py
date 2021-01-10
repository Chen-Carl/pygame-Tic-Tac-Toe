import sys
import pygame

from chessboard import Chessboard
from piece import Piece


def check_events(screen, chessboard, pieces, ai_settings, stats, play_button,
                 chessbook_button, retract_button, image_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            stats.add_new_piece = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            stats.mouse_x = mouse_x
            stats.mouse_y = mouse_y
            check_play_button(stats, play_button, mouse_x, mouse_y, pieces)
            check_chessbook_button(stats, chessbook_button, mouse_x, mouse_y,
                                   pieces)
            check_retract_button(stats, retract_button, mouse_x, mouse_y, pieces)
            check_image_button(stats, image_button, mouse_x, mouse_y, ai_settings)


def update_screen(ai_settings, screen, chessboard, pieces, play_button, stats,
                  chessbook_button, retract_button, image_button):
    screen.fill(ai_settings.bg_color)
    chessboard.blit_board()
    for piece in pieces.sprites():
        piece.blit_piece()
    if stats.game_active:
        retract_button.draw_button()
    if not stats.game_active:
        play_button.draw_button()
        chessbook_button.draw_button()
        image_button.draw_button()
    pygame.display.flip()


def new_piece(screen, chessboard, mouse_x, mouse_y, pieces, ai_settings,
              stats):

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
    if index >= 0 and stats.boxes_status[index] == 0:
        stats.stack.append(index)
        # get the position to place a new piece
        rect_x = chessboard.boxes[index][0] + 97
        rect_y = chessboard.boxes[index][1] + 192

        piece = Piece(screen, rect_x, rect_y, ai_settings, stats)
        pieces.add(piece)
        if stats.piece_choose == 1:
            stats.piece_choose = 0
            stats.boxes_status[index] = 2
        elif stats.piece_choose == 0:
            stats.piece_choose = 1
            stats.boxes_status[index] = 1
        judge_winner(chessboard, stats, ai_settings)

    elif i >= 0 and j >= 0 and stats.boxes_status[index] == 1:
        pass
    elif index < 0:
        pass


def judge_winner(chessboard, stats, ai_settings):
    win1 = stats.boxes_status[0] == stats.boxes_status[
        1] and stats.boxes_status[1] == stats.boxes_status[
            2] and stats.boxes_status[0] != 0
    win2 = stats.boxes_status[3] == stats.boxes_status[
        4] and stats.boxes_status[4] == stats.boxes_status[
            5] and stats.boxes_status[3] != 0
    win3 = stats.boxes_status[6] == stats.boxes_status[
        7] and stats.boxes_status[7] == stats.boxes_status[
            8] and stats.boxes_status[6] != 0
    win4 = stats.boxes_status[0] == stats.boxes_status[
        3] and stats.boxes_status[3] == stats.boxes_status[
            6] and stats.boxes_status[0] != 0
    win5 = stats.boxes_status[1] == stats.boxes_status[
        4] and stats.boxes_status[4] == stats.boxes_status[
            7] and stats.boxes_status[1] != 0
    win6 = stats.boxes_status[2] == stats.boxes_status[
        5] and stats.boxes_status[5] == stats.boxes_status[
            8] and stats.boxes_status[2] != 0
    win7 = stats.boxes_status[0] == stats.boxes_status[
        4] and stats.boxes_status[4] == stats.boxes_status[
            8] and stats.boxes_status[0] != 0
    win8 = stats.boxes_status[2] == stats.boxes_status[
        4] and stats.boxes_status[4] == stats.boxes_status[
            6] and stats.boxes_status[2] != 0
    win = [win1, win2, win3, win4, win5, win6, win7, win8]
    for i in range(8):
        if win[i]:
            print("Winner: ", stats.piece_choose)
            stats.game_active = False
            break
    no_wins = True
    for i in range(9):
        if stats.boxes_status[i] == 0:
            no_wins = False
            break
    if no_wins:
        print("Draw!")
        stats.game_active = False


def update_pieces(pieces, screen, chessboard, stats, ai_settings):
    if stats.add_new_piece:
        new_piece(screen, chessboard, stats.mouse_x, stats.mouse_y, pieces,
                  ai_settings, stats)


def check_play_button(stats, play_button, mouse_x, mouse_y, pieces):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        pieces.empty()

        stats.game_active = True


def check_chessbook_button(stats, chessbook_button, mouse_x, mouse_y, pieces):
    button_clicked = chessbook_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        print(pieces)

def check_retract_button(stats, retract_button, mouse_x, mouse_y, pieces):
    button_clicked = retract_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_active:
        tmp = [x for x in pieces]
        if len(tmp) > 0:
            pieces.remove(tmp[-1])
            stats.boxes_status[stats.stack[-1]] = 0
            del(stats.stack[-1])
            stats.piece_choose = not stats.piece_choose
            
def check_image_button(stats, image_button, mouse_x, mouse_y, ai_settings):
    button_clicked = image_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.image_series = (ai_settings.image_series + 1) % 3