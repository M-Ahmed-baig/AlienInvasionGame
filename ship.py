import pygame
from settings import Setting

class Ship():
    """Intialize the ship and set its starting point."""

    def __init__(self,screen,ai_settings:Setting):
        self.screen=screen
        self.image=pygame.image.load('images/space_ship.png')
        self.image= pygame.transform.scale(self.image, (40, 50))
        self.rect=self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Controls ship's right and left movement flags ,speed and update new 
        # position.
        self.moving_right = False
        self.moving_left = False
        self.center=float(self.rect.centerx)
        self.speed=ai_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
      
        """Update the ship's position based on the movement flag and ship right
         and left range."""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
            self.rect.centerx=self.center

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.speed
            self.rect.centerx=self.center
           
                 
                 
           
           
            


