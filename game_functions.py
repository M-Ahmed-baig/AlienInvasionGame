import sys
import pygame
# Import Ship just so Python/VSCode knows the type of the parameter
from ship import Ship

# (ship:Ship) means ship is the object of class Ship so vscode list its 
# attributes and methods.
def check_keydown_event(event,ship:Ship):
    """Check which key was pressed."""
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = True
    elif event.key ==pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_event(event,ship:Ship):
    """Check which key was released."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship:Ship):
    """Respond to keypresses/keyups and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ship)
                   
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        
    # keys=pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]:
    #     ship.ship_rect.centerx+=0.5

def update_screen(screen,ship,ai_settings):
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    pygame.display.flip()
    