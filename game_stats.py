class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, tp_game):
        """Initialize statistics"""
        self.settings = tp_game.settings
        self.rest_stats()
        # Start game in an inactive state
        self.game_active = False

    def rest_stats(self,):
        """Initialize statistics that can change during the game."""
        self.missed = self.settings.shoot_limit
