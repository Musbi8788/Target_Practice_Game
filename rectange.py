import pygame 

class Rectangle:
    """ A Class to create a rectangle
    """

    def __init__(self, tp_game):
        """Initialize the rectangle attributes"""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = self.screen.get_rect()

        # Set the dimenson and properties the of the rectangle
        self.width, self.height = 50, 200
        self.rectangle_color = (0, 0, 250)

        # Build the rectangle's rect object and center right it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right



        # Store the rectangle exact vertical position
        self.y = float(self.rect.y)

        self.vertical_direction = 1

    def check_edges(self):
        """Return True if rectangle is at edge of screen
        """
        # get the screen rect
        screen_rect = self.screen.get_rect()

        # checking the rectangle fleet position in the screen
        # determinding how to the rectangle should move on the screen
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True


    def update(self):
        """Move the rectangle left or right
        """
        # Reverst direction if it hit top to down
        if self.rect.top <= self.screen_rect.top:
            self.vertical_direction = 1
        
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.vertical_direction = -1

        # Update position of the rectangle rect
        self.y = self.settings.rectangle_speed * self.vertical_direction
        self.rect.y += self.y  

    def draw_rectangle(self):
        """Draw blank rectangle and then draw message"""
        self.screen.fill(self.rectangle_color, self.rect)  # draw the rectange
