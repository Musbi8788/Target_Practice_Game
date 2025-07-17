import sys
from time import sleep

import pygame

from ship import Ship
from settings import Settings
from bullets import Bullet
from rectange import Rectangle
from game_stats import GameStats
from button import Button


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

        # Create an instance to store the game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)

        # Make the bullets and rectangle in a pygame group form
        self.bullets = pygame.sprite.Group()

        self.rectangle = pygame.sprite.Group()
        self.rect_obj = Rectangle(self)


        self.rectangle.add(self.rect_obj)
    

        # make the play button
        self.play_button = Button(self, "Play")



    def run_game(self):
        """Respond to the running game."""
        game_is_running = True

        while game_is_running:
            self._check_events()

            if self.stats.game_active:
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

            elif event.type == pygame.MOUSEBUTTONDOWN:  # check for mouse click
                mouse_pos = pygame.mouse.get_pos()  # get the position of the mouse click
                self._check_play_button(mouse_pos)

    def _start_game(self):
        """Respond to start the game"""
        if not self.stats.game_active:  # Allow user to start the game if the game is inactive

            # Reset the game statistics
            self.stats.rest_stats()
            self.stats.game_active = True
            # Destory the bullets
            self.bullets.empty()
            # Create the ship and center left it 
            self.ship.center_left_ship()

            # Hide the mouse
            pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        # Only make the button clickable when the game is inactive
        if button_clicked and not self.stats.game_active:

            self._start_game()

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

            self._check_bullets_rectangle_collisions()
    
    def _check_bullets_rectangle_collisions(self):
        """Respond to bullets-rectangle collisions
        """
        # Remove any bullets and rectangle that have collided

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.rectangle, True, False)  




    def _update_screen(self):
        """Update the screen background and show the image 
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for rectangle in self.rectangle.sprites():
            rectangle.draw_rectangle()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()



if __name__ == "__main__":
    """Create an instance and run the game."""
    tp = TargetPractice()
    tp.run_game()