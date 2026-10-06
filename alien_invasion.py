import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullets import Bullet

def run_game():
    """Sets all game objects and run the game."""

    # Initialize pygame modules & Create Alien invasion settings object.
    pygame.init()
    ai_settings=Setting()

    # Create game window.
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship=Ship(screen,ai_settings)

    # Make a group to store bullets in.
    bullets=Group()

    # Define frame rate & Block mouse motion event.
    clock=pygame.time.Clock()
    pygame.event.set_blocked(pygame.MOUSEMOTION)
   
    # Game Loop.
    while True:
        gf.check_events(ship,ai_settings,bullets,screen)

        ship.update()

        bullets.update()

        print(bullets)

        gf.update_screen(screen,ship,ai_settings,bullets)

        clock.tick(100)
run_game()
