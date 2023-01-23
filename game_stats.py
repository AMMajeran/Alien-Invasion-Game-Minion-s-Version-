import json

class GameStats:
    """Monitoring statistics data in Minion's Invasion game"""
    def __init__(self, ai_game):
        """initialization statistics data"""
        self.settings = ai_game.settings
        self.reset_stats()
        #running game in unactive status
        self.game_active = False
        #best score should not be reset
        with open('bestscoreofalltime.txt') as score_file:
            self.high_score = json.load(score_file)

    def reset_stats(self):
        """initialization statistics data, which are variable during game""" 
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

