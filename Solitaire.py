import random
import pygame
from pygame.locals import *

ACE = 1
KING = 13
QUEEN = 12
JACK = 11

CLOVER = 1
SPADE = 2
HEART = 3
DIAMOND = 4

CARD_WIDTH = 85
CARD_HEIGHT = 110

def create_deck():
    # Deck of cards has 52 cards, 4 suites, and 2-10 jack, queen, king, ace
    # 11 = jack
    # 12 = queen
    # 13 = king
    # 1 = ace
    # random number from 1-13
    # Random number from 1-4 representing suite
    # Check that the card isn't in the deck yet
    # will return an array of 52 "cards"
    deck = []

    for i in range(52):
        card_val = random.randint(1, 13)  # 14 exclusive
        card_suite = random.randint(1, 4)
        card = create_card(card_val, card_suite)

        while card in deck:
            card_val = random.randint(1, 13)  # 14 exclusive
            card_suite = random.randint(1, 4)
            card = create_card(card_val, card_suite)

        deck.append(card)
    print('Done generating deck')
    return deck

def create_card(card_val, card_suite):
    # i know there is a better way to do this, might get to it might npt
    # better way involves puutting stuff into lists and gettings the card val based on that list
    if card_val == ACE:
        val = 'A'
    elif card_val == KING:
        val = 'K'
    elif card_val == QUEEN:
        val = 'Q'
    elif card_val == JACK:
        val = 'J'
    else:
        val = str(card_val)

    if card_suite == CLOVER:
        suite = 'C'
    elif card_suite == SPADE:
        suite = 'S'
    elif card_suite == HEART:
        suite = 'H'
    elif card_suite == DIAMOND:
        suite = 'D'
    else:
        suite = ''

    card = val + '-' + suite
    return card

def shuffle_deck(deck):
    # Pick a random int form 1 to 52 for each card and switch there places
    new_deck = []

    for i in range(len(deck)):
        rand_num = random.randint(0, len(deck)-1)

        while deck[rand_num] in new_deck:
            rand_num = random.randint(0, len(deck)-1)
        new_deck.append(deck[rand_num])

    return new_deck

def create_board():
    # Create 7 different piles, plus 4 for the different final sorting piles
    board = {  # easiest to represent the board with a dictionary
        "pile1": [], # add another array to show which cards are face up and which are not
        "pile2": [],
        "pile3": [],
        "pile4": [],
        "pile5": [],
        "pile6": [],
        "pile7": [],
        "pileH": [],
        "pileD": [],
        "pileS": [],
        "pileC": [],
        "pileE": [], # Deck pile
        "pileX": [], # Discard pile
        "pileZ": [] # Pile to hold the cards being carried
    }

    return board

def populate_board(deck, board):
    for pile in board:
        if pile[-1].isdigit():
            for i in range(int(pile[-1])): # Depending on the pile #, set a different amount to distribute
                board[pile].append(deck.pop(0)) # Always popping the first index because you are always drawing from the top of the deck
        elif pile == 'pileE':
            for card in deck: # Add the remaining cards to the deck
                board[pile].append(card)
    return board

def create_card_image(card):
    if '-' in card:
        card_val = card.split('-')[0]
        card_suite = card.split('-')[1]
        card_string = ''

        try:
            card_string = card_val + card_suite + '.png'
            card_image = pygame.image.load('Assets/' + card_string)
            card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
            return card_image
        except:
            print('Could not find card name: %s' % card_string)
            return None
    else:
        try:
            card_string = card + '.png'
            card_image = pygame.image.load('Assets/' + card_string)
            card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
            return card_image
        except:
            print('Could not find card name')
            return None

def draw_pile(pile_num, pile, display): # Pile number will signfy where we have to place the pile and the pile itself contains all the cards in said pile
    if pile_num.isdigit():
        pile_num = int(pile_num)
        pile_x = (CARD_WIDTH * (pile_num-1)) + (25 * pile_num)
        pile_y = 250  # Will change based on the current card (increase by 25)

        if len(pile) > 0:
            card_count = 0
            for card in pile:
                if card_count != (len(pile) - 1): # If the last card in the pile, display it
                    card_image = create_card_image('green_back')
                    display.blit(card_image, (pile_x, pile_y))
                else:
                    card_image = create_card_image(card)
                    display.blit(card_image, (pile_x, pile_y))
                card_count += 1
                pile_y += 25
        else:
            # draw a transparent rectangle where the pile would be
            pile_rect = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
            pile_rect.set_alpha(125)
            pile_rect.fill((0, 0, 0))
            display.blit(pile_rect, (pile_x, pile_y))
    else: # One of the other 6 piles
        pile_x = -1 # original offsets
        pile_y = -1

        # Change this to use constants
        if pile_num == 'H':
            pile_x = 50
            pile_y = 75
        elif pile_num == 'D':
            pile_x = CARD_WIDTH + 75
            pile_y = 75
        elif pile_num == 'C':
            pile_x = CARD_WIDTH*2 + 100
            pile_y = 75
        elif pile_num == 'S':
            pile_x = CARD_WIDTH*3 + 125
            pile_y = 75
        elif pile_num == 'X':
            pile_x = CARD_WIDTH*4 + 225
            pile_y = 25
        elif pile_num == 'E':
            pile_x = CARD_WIDTH*4 + 350
            pile_y = 25

        if len(pile) > 0:
            if pile_num == 'X': # discard pile
                # Display first 3 cards
                count = -1
                while count > -4:
                    card_image = create_card_image(pile[count])
                    display.blit(card_image, (pile_x, pile_y))
                    pile_y += 25
                    count -= 1
            elif pile_num != 'E' and pile_num != 'Z': # 4 ending piles
                for card in pile:
                    card_image = create_card_image(card)
                    display.blit(card_image, (pile_x, pile_y))
            else: # deck
                if pile_num != 'Z':
                    card_image = create_card_image('green_back')
                    display.blit(card_image, (pile_x, pile_y))
        else:
            if pile_num != 'Z': # don't render z pile here
                pile_rect = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
                pile_rect.set_alpha(125)
                pile_rect.fill((0, 0, 0))
                display.blit(pile_rect, (pile_x, pile_y))

def render_pile_z(mouse_location, pile, display):
    for card in pile:
        pile_x = mouse_location[0]
        pile_y = mouse_location[1]

        card_image = create_card_image(card)
        display.blit(card_image, (pile_x, pile_y))

def display_board(display, board):
    # 7 piles
    for pile in board:
        draw_pile(pile[-1], board[pile], display)

def deck_clicked(board):
    new_board = board.copy()
    # from the E pile, move 3 cards to the X pile
    if len(new_board['pileE']) > 0:
        for i in range(3):
            new_board['pileX'].append(new_board['pileE'].pop(0)) # Stay at index 0 to always be moving the top card o fthe deck
    else:
        # There are no cards left in the deck pile, so if this button is clicked...
        # Add all cards from pile X (discard pile) back into the deck pile
        for card in reversed(new_board['pileX']): # reversed because last card is first
            new_board['pileE'].append(new_board['pileX'].pop(new_board['pileX'].index(card)))

    return new_board

#def card_clicked(mouse_location, card_x, card_y):


def run(display):
    play_solitaire = True

    bg = pygame.image.load('Assets/main-menu-background.png')

    deck = create_deck()
    board = populate_board(deck, create_board()) # Create a new board and populate it

    card_clicked = False
    original_pile = ''

    while play_solitaire:
        # Event loop
        for event in pygame.event.get():  # loops through the events gathered by pygame
            if event.type == pygame.QUIT or event.type == KEYUP:  # Escape key to quit, mostly to speed up testing/development
                # If the window is closed, shutdown all of pygame and don't run the next function
                # which is what would happen if display_main_menu was set to true
                if event.key is K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == MOUSEBUTTONUP:  # When the mouse is released
                mouse_location = pygame.mouse.get_pos()  # Get the current location

                # Loop through all the last cards in each pile and get there rectangles
                if Rect((CARD_WIDTH*4 + 350), 25, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):
                    board = deck_clicked(board)

                if card_clicked:
                    card_clicked = False
                    board[original_pile].append(board['pileZ'].pop(0)) # This will have to change to accomdate piles with multiple cards
                    original_pile = ''

            elif event.type == MOUSEBUTTONDOWN:
                # (CARD_WIDTH * (pile_num-1)) + (25 * pile_num)
                mouse_location = pygame.mouse.get_pos()  # Get the current location
                if Rect(25, 250, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location): #1
                    if len(board['pile1']) > 0:
                        card_clicked = True
                        original_pile = 'pile1'
                        board['pileZ'].append(board['pile1'].pop(0))
                elif Rect((CARD_WIDTH + (25 * 2)), 275, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):  # 2
                    print('Clicked 2')
                elif Rect(((CARD_WIDTH * 2) + (25 * 3)), 300, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):  # 3
                    print('Clicked 3')
                elif Rect(((CARD_WIDTH * 3) + (25 * 4)), 325, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):  # 4
                    print('Clicked 4')
                elif Rect(((CARD_WIDTH * 4) + (25 * 5)), 350, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):  # 5
                    print('Clicked 5')
                elif Rect(((CARD_WIDTH * 5) + (25 * 6)), 375, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):  # 6
                    print('Clicked 6')
                elif Rect(((CARD_WIDTH * 6) + (25 * 7)), 400, CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_location):  # 7
                    print('Clicked 7')
            elif event.type == MOUSEMOTION:
                if card_clicked:
                    # Render pile z
                    print('rendering z')


                # If the location is within that of the deck pile
                # How to get location of deck pile

                # If a card is clicked, form a rectanlge with the bottom right corner being that of where the cursor is
                # knowing this, we should be able to find the length and height of this rectanlge, so whenever the cursor moves adjuist it accordingly

        # Each game loop, display board
        # Have a pile to represent the deck
        # display last 3 cards
        # Draggable cards to the pile they want?
        # If the card is compatible with t e pile lock onto it
        # Otherwise snap back to the deck

        display.blit(bg, (0, 0))

        # Display board
        display_board(display, board)

        if card_clicked:
            render_pile_z(pygame.mouse.get_pos(), board['pileZ'], display)

        pygame.display.update()
