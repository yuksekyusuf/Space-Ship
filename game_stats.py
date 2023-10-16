class GameStats:
    """Track statistics for Space Ship"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
    
    def reset_stats(self):
        """Initializez statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        