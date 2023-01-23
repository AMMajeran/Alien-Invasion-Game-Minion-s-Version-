import pygame

class Settings:
    """A class desgined to store all game settings"""

    def __init__(self):
        """Initialization game settings."""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (17, 86, 149)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3 

        #bullet settings
        self.bullet_speed =0.1
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = (255, 214, 77)
        self.bullet_allowed = 5

        #alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 5

        #Value of fleet_direction 1 define right direction, -1 define left direction
        self.fleet_direction = 1

        #easy way to change game speed
        self.speedup_scale = 1.1
        #easy change points amount that player gets for hit an alien
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialization settings which will change during game"""
        self.ship_speed = 2
        self.bullet_speed = 3 
        self.alien_speed = 0.5
        self.fleet_direction = 1 
        self.alien_points = 10

    def increase_speed(self):
        """Changing object speed settings and increasing points amount for hit an alien"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

        

