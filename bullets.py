import pygame
from pygame.sprite import Sprite
from settings import Setting
from ship import Ship

class Bullet(Sprite):
    """ Manage bullet's starting position,movement etc."""
    def __init__(self,ship:Ship,ai_settings:Setting,screen):
        super().__init__() 
        self.screen = screen
        self.setting = ai_settings
        self.bullet_rect = pygame.Rect(0,0,self.setting.bullet_width,
                                       self.setting.bullet_height)
        

        self.bullet_rect.centerx = ship.ship_rect.centerx
        self.bullet_rect.bottom = ship.ship_rect.top
        self.bullet_speed = ai_settings.bullet_speed_factor
        self.bullet_color = ai_settings.bullet_color

        self.y = float(self.bullet_rect.y)



    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.y -= self.bullet_speed

        # Update the rect position
        self.bullet_rect.y = self.y

        #Remove this Sprite from all Groups it belongs to. if it goes out of 
        # the screen.
        if self.bullet_rect.bottom <= 0:
            self.kill()

    def draw_bullet(self):
        """Move the bullets up the screen."""
        pygame.draw.rect(self.screen ,self.setting.bullet_color ,
                    self.bullet_rect)
            


        
