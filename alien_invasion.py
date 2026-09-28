import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game,settings,Ship and create a screen object and block mouse
    # motion event.
    pygame.init()
    ai_settings=Setting()
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(screen,ai_settings)
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    clock=pygame.time.Clock()

    # Start the main loop for the game.
    while True:
        # Call event loop function.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen,ship,ai_settings)
        clock.tick(60)
run_game()
