import pygame
from pygame.sprite import Sprite
from settings import Setting

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self,screen ,ai_setting:Setting):
        super().__init__()
        # Load the image and get its rect.
        self.screen = screen
        self.setting = ai_setting
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set rect position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.self.rect)

    def update(self):
        """Move the alien right or left."""
        self.x += (self.setting.alien_speed_factor *
                self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


            






