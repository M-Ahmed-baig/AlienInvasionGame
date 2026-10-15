class Setting():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):

        # Screen settings
        self.width = 850
        self.height = 600
        self.bg_color = (82,140,211)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_height = 8
        self.bullet_width = 4
        self.bullet_color = (226, 88, 34)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1