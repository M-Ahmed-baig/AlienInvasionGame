import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """Sets all game objects and run the game."""

    # Initialize pygame modules & Create Alien invasion settings object.
    pygame.init()
    ai_settings=Setting()

    # Create game window.
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen,ai_settings) 

    # Make a group to store bullets in.
    bullets = Group()

    # Make a alien.
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(screen ,aliens ,ai_settings ,ship.rect.height)
    
    # Define frame rate & Block mouse motion event.
    clock=pygame.time.Clock()
    pygame.event.set_blocked(pygame.MOUSEMOTION)
  

    # Game Loop.
    while True:
        gf.check_events(ship, ai_settings, bullets, screen)
       
        ship.update()

        bullets.update()

        gf.check_alien_bullet_collision(bullets, screen, aliens, ai_settings,
                                    ship.rect.height)

        gf.update_aliens(screen, ai_settings, aliens, ship, bullets)

        gf.update_screen(screen, ship, ai_settings, bullets, aliens)

        clock.tick(100)
run_game()
 