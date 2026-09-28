import pygame
from settings import Setting

class Ship():
    """Intialize the ship and set its starting point."""

    def __init__(self,screen,ai_settings:Setting):
        self.screen=screen
        self.image=pygame.image.load('images/space_ship.png')
        self.image= pygame.transform.scale(self.image, (50, 60))
        self.ship_rect=self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.screen_rect = screen.get_rect()
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # Controls ship's right and left movement flags ,speed and update new 
        # position.
        self.moving_right = False
        self.moving_left = False
        self.center=float(self.ship_rect.centerx)
        self.speed=ai_settings.ship_speed_factor

    def blit_me(self):
        self.screen.blit(self.image,self.ship_rect)

    def update(self):
      
        """Update the ship's position based on the movement flag and ship right
         and left range."""
        
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += self.speed
            self.ship_rect.centerx=self.center

        if self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.center -= self.speed
            self.ship_rect.centerx=self.center
           
                 
                 
           
           
            


