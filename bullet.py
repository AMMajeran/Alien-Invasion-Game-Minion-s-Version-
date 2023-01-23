import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class designed to manage bullets fired  by the ship"""

    def __init__(self, ai_game):
        """creating bullet object at current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
    
        #creating a bullet rect. at (0, 0) and then defining the appropiate postion for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Bullet position is defined by floating number value
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullet on screen"""
        #updating bullet position
        self.y -= self.settings.bullet_speed
        #updating bullet's rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Displaying bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)