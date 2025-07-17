import sys
import pygame

from ship import Ship
from settings import Settings
from bullets import Bullet
from rectange import Rectangle


class TargetPractice():
    """A class to manage the Target Practice"""

    def __init__(self):
        """Initialize the target parctice attributes and set the game resources."""

        pygame.init()
        self.settings = Settings()

        # Defualt screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption(self.settings.game_title)

        self.ship = Ship(self)

        # Make the bullets and aliens in a pygame group form
        self.bullets = pygame.sprite.Group()

        self.rectangle = Rectangle(self)


        

    def run_game(self):
        """Respond to the running game."""
        game_is_running = True
        while game_is_running:
            self._check_events()
            self.rectangle.update()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypress
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress
        """
        # move the ship up
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key release
        """
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group
        """
        # Limit the bullets showing in the game screen
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullet and get rid of the old bullet
        """
        # Get rid of bullets that has disappeared
        for bullet in self.bullets.copy():
            # place i get stuck with
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)



    def _update_screen(self):
        """Update the screen background and show the image 
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rectangle.draw_rectangle()
        pygame.display.flip()



if __name__ == "__main__":
    """Create an instance and run the game."""
    tp = TargetPractice()
    tp.run_game()