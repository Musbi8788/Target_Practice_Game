class Settings:
    """A class to set the settings for the game
    """

    def __init__(self):
        """Initialize for the game
        """

        # Bullets Settings
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (75, 0, 130)
        self.bullets_allowed = 5

        # Ship Settings
        self.ship_speed = 1.5
        # self.ship_limit = 3  # number of live the user have

        # Screen Settings
        self.screen_width = 850  # defualt 850
        self.screen_height = 650  # 650
        self.bg_color = (130, 200, 229)
        self.game_title = "Target Practice"

        # Rectangle 
        self.rectangle_speed = 1.5
        self.fleet_drop_speed = 10
        self.vertical_direction = 1

        # Three change to loss
        self.shoot_limit = 3
