import pygame # Imports pygame and all its methods, attributes and classes
from pygame.locals import * # Imports key constants to decode key press events (really just makes less to type... pygame.KEYDOWN vs KEYDOWN)
import time
import random
import Solitaire
import Blackjack
import GinRummy

# Initialize pygame
pygame.init()

# Variables to hold the display width and height
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Variables to hold different font presets
HEADER_FONT = pygame.font.SysFont('frenchscript', 75)
TEXT_FONT = pygame.font.SysFont('frenchscript', 55)
BUTTON_FONT = pygame.font.SysFont('frenchscript', 55)

# Button constants
BUTTON_WIDTH = 350
BUTTON_HEIGHT = 75
BUTTON_WIDTH_PADDING = 35
BUTTON_HEIGHT_PADDING = 15

# Setup color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Game option constants
SOLITAIRE = 1
BLACK_JACK = 2
GIN_RUMMY = 3

# Pygame specific variables such as the display "surface", window title, and the clock
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Card game suite')
bg = pygame.image.load('Assets/main-menu-background.png')
clock = pygame.time.Clock()

# Function to print all of the fonts
def print_fonts():
    for font in pygame.font.get_fonts():
        print(font)

# Will run the individual game code
def game_loop():
    run_game = True
    user_game = 0

    while run_game:
        if user_game == 0:
            display_main_menu = True

            # Pre render text and other shapes
            # The header text / bounding rectangle
            header_text = HEADER_FONT.render('Choose a game to play!', True,
                                             BLACK)  # Creates a surface for this text to be drawn on the screen
            header_rect = header_text.get_rect()  # Gets the rectantgle surroudnign the text
            header_rect_x = (
                                        DISPLAY_WIDTH / 2) - header_rect.centerx  # Subtract the center of the screen with the center of the texts' rectangle to display the text in the center of the screen
            header_rect_y = 50 - header_rect.centery  # Same concept here except not half the screen, only a few pixels below the top of the screen (y=0)
            # header_width = header_rect.width
            # header_height = header_rect.height

            # Solitaire text and bounding rectangle
            sol_text = BUTTON_FONT.render('Solitaire', True, BLACK)
            sol_rect = sol_text.get_rect()
            sol_rect_x = (DISPLAY_WIDTH / 2) - sol_rect.centerx
            sol_rect_y = 200 - sol_rect.centery  # increment buttons by 100px apart
            sol_width = sol_rect.width
            sol_height = sol_rect.height
            # The final rectangle has some added padding, so must save it as its own!
            sol_final_rect = ((sol_rect_x - (BUTTON_WIDTH_PADDING / 2)), (sol_rect_y - (BUTTON_HEIGHT_PADDING / 2)),
                              (sol_width + BUTTON_WIDTH_PADDING), (sol_height + BUTTON_HEIGHT_PADDING))

            # Black jack text and bounding rectangle
            bj_text = BUTTON_FONT.render('Black jack', True, BLACK)
            bj_rect = bj_text.get_rect()
            bj_rect_x = (DISPLAY_WIDTH / 2) - bj_rect.centerx
            bj_rect_y = 300 - bj_rect.centery
            bj_width = bj_rect.width
            bj_height = bj_rect.height
            bj_final_rect = ((bj_rect_x - (BUTTON_WIDTH_PADDING / 2)), (bj_rect_y - (BUTTON_HEIGHT_PADDING / 2)),
                             (bj_width + BUTTON_WIDTH_PADDING), (bj_height + BUTTON_HEIGHT_PADDING))

            # gin Rummy text and bounding rectangle
            gr_text = BUTTON_FONT.render('Gin rummy', True, BLACK)
            gr_rect = gr_text.get_rect()
            gr_rect_x = (DISPLAY_WIDTH / 2) - gr_rect.centerx
            gr_rect_y = 400 - gr_rect.centery
            gr_width = gr_rect.width
            gr_height = gr_rect.height
            gr_final_rect = ((gr_rect_x - (BUTTON_WIDTH_PADDING / 2)), (gr_rect_y - (BUTTON_HEIGHT_PADDING / 2)),
                             (gr_width + BUTTON_WIDTH_PADDING), (gr_height + BUTTON_HEIGHT_PADDING))

            # Main menu loop
            while display_main_menu:
                for event in pygame.event.get():  # loops through the events gathered by pygame
                    if event.type == pygame.QUIT or event.type == KEYUP:  # Escape key to quit, mostly to speed up testing/development
                        # If the window is closed, shutdown all of pygame and don't run the next function
                        # which is what would happen if display_main_menu was set to true
                        if event.key is K_ESCAPE:
                            pygame.quit()
                            quit()
                    elif event.type == MOUSEBUTTONUP:  # When the mouse is released
                        mouse_location = pygame.mouse.get_pos()  # Get the current location

                        # Check if the location of that click collided with any of the rectangles that were created above
                        if Rect(sol_final_rect).collidepoint(mouse_location):  # Create a Rect object so that we can access the collidepoint() function
                            display_main_menu = False  # Stops the loop from running, letting us move into the game loop
                            user_game = 1  # Sets the game the user wants to play, broken down by a unique number
                        elif Rect(bj_final_rect).collidepoint(mouse_location):
                            display_main_menu = False
                            user_game = 2
                        elif Rect(gr_final_rect).collidepoint(mouse_location):
                            display_main_menu = False
                            user_game = 3

                # Draw/"blit" stuff here
                game_display.blit(bg, (0, 0))  # Draws the background image to the background

                # Header
                # pygame.draw.rect(game_display, WHITE, (header_rect_x, header_rect_y, header_width, header_height)) # Don't really need to show
                game_display.blit(header_text, (header_rect_x, header_rect_y))  # Write the text to the screen

                # Solitaire button
                pygame.draw.rect(game_display, BLACK, sol_final_rect, 1)
                game_display.blit(sol_text, (sol_rect_x, sol_rect_y))

                # Black jack button
                pygame.draw.rect(game_display, BLACK, bj_final_rect, 1)
                game_display.blit(bj_text, (bj_rect_x, bj_rect_y))

                # Gin rummy button
                pygame.draw.rect(game_display, BLACK, gr_final_rect, 1)
                game_display.blit(gr_text, (gr_rect_x, gr_rect_y))

                # Update the screen
                pygame.display.update()
        elif user_game == 1:
            for event in pygame.event.get():  # loops through the events gathered by pygame
                if event.type == pygame.QUIT or event.type == KEYUP:  # Escape key to quit, mostly to speed up testing/development
                    # If the window is closed, shutdown all of pygame and don't run the next function
                    # which is what would happen if display_main_menu was set to true
                    if event.key is K_ESCAPE:
                        pygame.quit()
                        quit()
            Solitaire.run(game_display)
        elif user_game == 2:
            for event in pygame.event.get():  # loops through the events gathered by pygame
                if event.type == pygame.QUIT or event.type == KEYUP:  # Escape key to quit, mostly to speed up testing/development
                    # If the window is closed, shutdown all of pygame and don't run the next function
                    # which is what would happen if display_main_menu was set to true
                    if event.key is K_ESCAPE:
                        pygame.quit()
                        quit()
            Blackjack.main()
            for event in pygame.event.get():  # loops through the events gathered by pygame
                if event.type == pygame.QUIT or event.type == KEYUP:  # Escape key to quit, mostly to speed up testing/development
                    # If the window is closed, shutdown all of pygame and don't run the next function
                    # which is what would happen if display_main_menu was set to true
                    if event.key is K_ESCAPE:
                        pygame.quit()
                        quit()
        elif user_game == 3:
            GinRummy.main()

def main():
    #print_fonts()
    game_loop()
    pygame.quit()
    quit()


main()
