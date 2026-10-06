class Setting():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
   
        self.width = 800
        self.height = 600
        self.bg_color = (135, 206, 235)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_height = 9
        self.bullet_width = 9
        self.bullet_color = (226, 88, 34)
        self.bullets_allowed = 3