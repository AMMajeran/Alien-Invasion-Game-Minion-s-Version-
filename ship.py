import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """class designed to ship manage"""

    def __init__(self, ai_game):
        """ship Initialization and its initial position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Loading ship image and download its square
        self.image = pygame.image.load('images/minion.bmp')
        self.rect = self.image.get_rect()

        #each new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #the ship's horizontal position is stored as a floating point number
        self.x = float(self.rect.x)

        #ship movement options
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updating the position of the ship based on the option indicating its movement"""
        #update  ship's X coordinate value, not its rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update the rect object based on the value of self.x
        self.rect.x = self.x 

    def blitme(self):
        """Displaying ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """put ship center on the screen lower edge"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        