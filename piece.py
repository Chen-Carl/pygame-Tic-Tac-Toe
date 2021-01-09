import pygame
from pygame.sprite import Sprite

class Piece(Sprite):
    def __init__(self, screen, rect_x, rect_y):
        super().__init__()
        self.screen = screen
        # if self.choose == 0:
        self.image = pygame.image.load("images/circle.png")
        # elif self.choose == 1:
        #     self.image = pygame.image.load("images/cross.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = rect_x
        self.rect.bottom = rect_y

    def blit_piece(self):
        self.screen.blit(self.image, self.rect)
