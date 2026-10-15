import sys
import pygame
# Import Ship & Setting just so Python/VSCode knows the type of 
# the parameter
from ship import Ship
from bullets import Bullet
from settings import Setting
from alien import Alien

# (ship:Ship) means ship is the object of class Ship so vscode list its 
# attributes and methods.

def fire_bullet(bullets ,ai_settings ,ship ,screen):
    "Create a new bullet and add it to the bullets group."
    if len(bullets) < ai_settings.bullets_allowed:
        bullet=Bullet(ship ,ai_settings ,screen)
        bullets.add(bullet)

def update_bullet(aliens, bullets):
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    pass

def check_keydown_event(event ,ship:Ship ,ai_settings ,bullets ,screen):
    """Check which key was pressed."""
    if event.key == pygame.K_SPACE:
        fire_bullet(bullets ,ai_settings ,ship ,screen)

    elif event.key == pygame.K_RIGHT: 
        ship.moving_right = True

    elif event.key ==pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event ,ship:Ship):
    """Check which key was released."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship:Ship ,ai_settings ,bullets ,screen):
    """Respond to keypresses/keyups and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event ,ship ,ai_settings ,bullets ,screen)
                   
        elif event.type == pygame.KEYUP:
            check_keyup_event(event ,ship)

def get_number_alien(screen ,alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space = screen.get_width() - (2*alien_width)
    number_of_aliens = int(available_space / (2*alien_width))
    return number_of_aliens

def get_number_rows(screen ,alien_height ,ship_height):
    """Determine the number of rows of aliens."""
    available_height = screen.get_height() - 3*alien_height - ship_height
    no_of_rows = int(available_height / (2*alien_height))
    return no_of_rows

def create_alien(alien_number ,screen ,aliens ,alien_width ,rect_y ,ai_setting):
    """Create an alien ,positioned it and store it in the group."""
    alien = Alien(screen ,ai_setting)
    alien.rect.y = rect_y
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    aliens.add(alien)

def create_row(row_number ,alien_height):
    return alien_height + (2*alien_height*row_number)
    
def create_fleet(screen ,aliens ,ai_setting ,ship_height):
    """Create a full fleet of aliens."""
    alien = Alien(screen ,ai_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    number_of_aliens = get_number_alien(screen ,alien_width)
    number_of_rows = get_number_rows(screen ,alien_height ,ship_height)

    for row in range(number_of_rows):
        rect_y = create_row(row ,alien_height)
        for alien_number in range(number_of_aliens):
            create_alien(alien_number ,screen ,aliens ,alien_width ,rect_y ,
                        ai_setting)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
         alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """
    Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def update_screen(screen ,ship:Ship ,ai_settings:Setting ,bullets ,aliens):
    " Update the game screen every frame."
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    aliens.draw(screen)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
  
    pygame.display.flip()
    