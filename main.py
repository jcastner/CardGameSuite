import pygame # Imports pygame and all its methods, attributes and classes
from pygame.locals import * # Imports key constants to decode key press events (really just makes less to type... pygame.KEYDOWN vs KEYDOWN)
import time
import random

pygame.init() # Initialize pygame

# Variables to hold the display width and height
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Variables to hold different font presets
HEADER_FONT = pygame.font.Font('freesansbold.ttf', 48)
TEXT_FONT = pygame.font.Font('freesansbold.ttf', 55)
BUTTON_FONT = pygame.font.Font('freesansbold.ttf', 35)

# Button constants
BUTTON_WIDTH = 350
BUTTON_HEIGHT = 75

# Setup color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
background = GREEN

# Pygame specific variables such as the display "surface", window title, and the clock
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Card game suite')
clock = pygame.time.Clock()

# Text object, to handle drawing text easier
class Text:
    def __init__(self):
        self.font_name = None
        self.font_size = 36
        self.font_color = BLACK
        self.background = None
        self.italic = False
        self.bold = False
        self.underline = False

    # Set the font and its properties.
    def set_font(self):
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)
        self.font.set_underline(self.underline)

    # Render the text into an image.
    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor, self.background)
        self.rect.size = self.img.get_size()
# Function to handle the games main menu
def main_menu():
    display_main_menu = True

    # Pre render text and other shapes
    header = HEADER_FONT.render('card game', True, BLACK)
    header_rect = header.get_rect()
    pygame.draw.rect(header, WHITE, header_rect)

    while display_main_menu:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT or event.type == KEYUP:
                # If the window is closed, shutdown all of pygame and don't run the next function
                # which is what would happen if display_main_menu was set to true
                if event.key is K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == MOUSEBUTTONUP:
                print('Mouse down')

        # Draw/"blit" stuff here
        game_display.fill(background)
        game_display.blit(header, (20, 100))

        # Update the screen and tick
        pygame.display.update()
        clock.tick(15)


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def main():
    main_menu()
    game_loop()
    pygame.quit()
    quit()


main()
