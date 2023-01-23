import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class designed to describe one minion soldier of army"""
    
    def __init__(self, ai_game):
        """Initialization minion soldier and define it's primary position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 

        #Loading minion image and define its rect atribute
        self.image = pygame.image.load('images/gru.bmp')
        self.rect = self.image.get_rect()

        #Place new minion soldier next to screen's left higher corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storage precision horizontal position of minion soldier
        self.x = float(self.rect.x)

    
    def update(self):
        """moving soldier to the right or to the left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns True value if soldier touches edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
