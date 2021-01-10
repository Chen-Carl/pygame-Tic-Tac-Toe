import pygame


class Chessboard():
    def __init__(self, screen):
        self.screen = screen

        box1 = [50, 50, 195, 195]
        box2 = [50, 250, 195, 195]
        box3 = [50, 450, 195, 195]
        box4 = [250, 50, 195, 195]
        box5 = [250, 250, 195, 195]
        box6 = [250, 450, 195, 195]
        box7 = [450, 50, 195, 195]
        box8 = [450, 250, 195, 195]
        box9 = [450, 450, 195, 195]
        self.boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

    def blit_board(self):
        for i in range(0, 9):
            pygame.draw.rect(self.screen, [0, 0, 0], self.boxes[i], 3)
