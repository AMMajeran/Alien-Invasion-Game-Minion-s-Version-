import pygame.font
import json
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """class designed to show information about score"""

    def __init__(self, ai_game):
        """initialization score atributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings for score informations
        self.text_color = (255, 213, 94)
        self.font = pygame.font.SysFont(None, 25)

        #prepare primary score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """Transform score in generated image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "POINTS:  " "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #displaying score in right hight corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def show_score(self):
        """displaying score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """conversion best score in generated image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str ="BEST SCORE:  " "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        #saves best score as text file  
        with open('bestscoreofalltime.txt', 'w') as score_file:
            json.dump(high_score, score_file)
           


        #displaying best score in the middle of screen, and by the top edge of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """checking if we have new best score achieved in game so far"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Conversion level numer in generated image"""
        level_str = "LVL: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #level number is displayed under current score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 

    def prep_ships(self):
        """displays amount of ships that left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10  + ship_number * ship.rect.width
            ship.rect.y = -10
            self.ships.add(ship)

