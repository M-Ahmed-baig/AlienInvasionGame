import sys
import pygame
# Import Ship & Setting just so Python/VSCode knows the type of 
# the parameter
from ship import Ship
from bullets import Bullet
from settings import Setting

# (ship:Ship) means ship is the object of class Ship so vscode list its 
# attributes and methods.
def fire_bullet(bullets,ai_settings,ship,screen):
    "Create a new bullet and add it to the bullets group."
    if len(bullets) < ai_settings.bullets_allowed:
        bullet=Bullet(ship,ai_settings,screen)
        bullets.add(bullet)

def check_keydown_event(event,ship:Ship,ai_settings,bullets,screen):
    """Check which key was pressed."""
    if event.key == pygame.K_SPACE:
        fire_bullet(bullets,ai_settings,ship,screen)

    elif event.key == pygame.K_RIGHT: 
        ship.moving_right = True

    elif event.key ==pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_event(event,ship:Ship):
    """Check which key was released."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship:Ship,ai_settings,bullets,screen):
    """Respond to keypresses/keyups and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ship,ai_settings,bullets,screen)
                   
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(screen,ship:Ship,ai_settings:Setting,bullets):
    " Update the game screen every frame."
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()
    