import pygame
from pygame.sprite import Sprite


class Piece(Sprite):
    def __init__(self, screen, rect_x, rect_y, ai_settings, stats):
        super().__init__()
        self.screen = screen
        if ai_settings.image_series == 0:
            if not stats.piece_choose:
                self.image = pygame.image.load("images/circle.png")
            else:
                self.image = pygame.image.load("images/cross.png")
        elif ai_settings.image_series == 1:
            if not stats.piece_choose:
                self.image = pygame.image.load("images/zdf1.png")
            else:
                self.image = pygame.image.load("images/lgx1.png")
        elif ai_settings.image_series == 2:
            if not stats.piece_choose:
                self.image = pygame.image.load("images/zdf2.png")
            else:
                self.image = pygame.image.load("images/lgx2.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = rect_x
        self.rect.bottom = rect_y

    def blit_piece(self):
        self.screen.blit(self.image, self.rect)
