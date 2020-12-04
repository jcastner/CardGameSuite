# Paul Tanny
# CS 021
# Final Project
# Blackjack game


# import modules
import random

# have to create the deck of cards
# ascii constants for suits
SPADES = '\u2660'
CLUBS = '\u2663'
DIAMONDS = '\u2666'
HEARTS = '\u2665'
# define ranks and suits
suits = (CLUBS, HEARTS, DIAMONDS, SPADES)
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# empty card deck list
card_deck = []


# deck of cards function
def deck_cards(suits, ranks):
    # create deck of cards
    for x in suits:
        for y in ranks:
            card_deck.append([x + y])
    # shuffle the card deck
    random.shuffle(card_deck)


# main function
def main():
    # define user and computer total and hands
    user_score = 0
    computer_score = 0
    user_hand = []
    computer_hand = []

    # have to get the deck of cards
    deck_cards(ranks, suits)

    # now have to deal
    #   user hand
    user_hand += deal(card_deck)
    user_hand += deal(card_deck)

    #   computer hand
    computer_hand += deal(card_deck)
    computer_hand += deal(card_deck)

    # get values for cards
    #   user cards
    user_card1 = value(user_hand[0])
    user_card2 = value(user_hand[1])

    #   computer cards
    computer_card1 = value(computer_hand[0])
    computer_card2 = value(computer_hand[1])

    # add values to score
    user_score += user_card1 + user_card2
    computer_score += computer_card1 + computer_card2

    # check to see if user won the game
    if user_score == 21 and user_score != computer_score:
        # if user won:
        print('Your hand:', user_hand)
        print('Dealers hand:', computer_hand)
        print('Congragulations! You got Blackjack!')
        # return to main menu
    # check to see if computer won the game
    elif computer_score == 21 and user_score != computer_score:
        # if computer won
        print('Your hand:', user_hand)
        print('Dealers hand:', computer_hand)
        print('Dealer won this hand. Better luck next time!')
        # return to main menu
    # check to see if both won the game
    elif computer_score == 21 and user_score == 21:
        # if tie game
        print('Your hand:', user_hand)
        print('Dealers hand:', computer_hand)
        print('This game was a tie. Both you and the dealer got Blackjack!')
        # return to main menu

    # if user/computer gets 2 aces
    # one ace will be worth 1 instead of 10
    elif user_score > 21:
        user_score -= 10

    elif computer_score > 21:
        computer_score -= 10

    # if neither won, ask user if they would like to hit
    else:
        print('Your hand:', user_hand)
        choice = input('Hit? (Y/N):')

        # if the user chooses not to hit, computer will hit until score is >= 17
        while choice.upper() == 'N':
            while computer_score <= 16:
                # getting next card
                next_card = deal(card_deck)
                # adding card to deck
                computer_hand += next_card
                # adding value of card to score
                computer_score += value(next_card[0])

            # check to see if user/computer won the game

            # if user hand is greater than computer hand, and less than 21
            if user_score > computer_score and user_score <= 21:
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('Congragulations! You won Blackjack!')
                # return to main menu

            # if user hand is less than computer hand, and less than 21
            elif user_score < computer_score and computer_score <= 21:
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The dealer won this hand. Better luck next time!')
                # return to main menu

            # if user hand is less, but dealer hand is over 21
            elif user_score < computer_score and computer_score > 21:
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('Congragulations! You won Blackjack!')
                # return to main menu

            # if computer hand is less, but user hand is over 21
            elif computer_score < user_score and user_score > 21:
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The dealer won this hand. Better luck next time')
                # return to main menu



            # if hands are equal
            elif user_score == computer_score and user_score <= 21:
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The game was a tie!')
                # return to main menu
            break

        # if the user chooses to hit,
        while choice.upper() == 'Y':
            # get another card from deck
            unext_card = deal(card_deck)
            # add card to user hand
            user_hand += unext_card
            # add value of user card to user score
            user_score += value(unext_card[0])
            # auto-hit for the computer
            while computer_score <= 16:
                next_card = deal(card_deck)
                computer_hand += next_card
                computer_score += value(next_card[0])

            # check to see if any one won

            if user_score >= 22 and computer_score <= 21:
                # computer won
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The dealer won this hand. Better luck next time')
                # return to main menu

            elif user_score <= 21 and computer_score >= 22:
                # user won
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('Congragulations! You won Blackjack!')
                # return to main menu

            elif user_score >= 22 and computer_score >= 22:
                # tie game
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The game was a tie. Both you and the dealer busted 21.')
                # return to main menu

            elif user_score == 21 and user_score != computer_score:
                # user won
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('Congragulations! You got Blackjack!')
                # reutnr to main menu

            elif user_score == 21 and user_score == computer_score:
                # tie game
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The game was a tie. Both you and the dealer got Blackjack!')
                # return to main menu

            elif user_score != computer_score and computer_score == 21:
                # computer won
                print('Your hand:', user_hand)
                print('Dealers hand:', computer_hand)
                print('The dealer won this hand. Better luck next time')
                # return to main menu

            # if no one won the game,
            else:
                # ask user if they would like to hit again
                print('Your hand:', user_hand)
                choice = input('Hit? (Y/N):')

                # I realize this is not the most effiecent way to do this, but I tried many other solutions trying to make it loop through or
                # to put it into a function that would be contionusly called when the user chose yes, but that didn't work
                # the only way I could do it with the way my code was written is by repeating this block of code

                # if user picked no
                while choice.upper() == 'N':
                    # if user hand is greater than computer hand, and less than 21
                    if user_score > computer_score and user_score <= 21:
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('Congragulations! You won Blackjack!')
                        # return to main menu

                    # if user hand is less than computer hand, and less than 21
                    elif user_score < computer_score and computer_score <= 21:
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('The dealer won this hand. Better luck next time!')
                        # return to main menu

                    # if user hand is less, but dealer hand is over 21
                    elif user_score < computer_score and computer_score > 21:
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('Congragulations! You won Blackjack!')
                        # return to main menu

                    # if computer hand is less, but user hand is over 21
                    elif computer_score < user_score and user_score > 21:
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('The dealer won this hand. Better luck next time')
                        # return to main menu


                    # if hands are equal
                    elif user_score == computer_score and user_score <= 21:
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('The game was a tie!')
                        # return to main menu
                    else:
                        print('Somethin else happened fam')
                    break

                # while choice is yes, hit for user
                while choice.upper() == 'Y':
                    unext_card = deal(card_deck)
                    user_hand += unext_card
                    user_score += value(unext_card[0])

                    # check to see if anyone won the game
                    if user_score >= 22 and computer_score <= 21:
                        # computer won
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('The dealer won this hand. Better luck next time')
                        # return to main menu

                    elif user_score <= 21 and computer_score >= 22:
                        # user won
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('Congragulations! You won Blackjack!')
                        # return to main menu

                    elif user_score >= 22 and computer_score >= 22:
                        # tie game
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('The game was a tie. Both you and the dealer busted 21.')
                        # return to main menu

                    elif user_score == 21 and user_score != computer_score:
                        # user won
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('Congragulations! You got Blackjack!')
                        # reutnr to main menu

                    elif user_score == 21 and user_score == computer_score:
                        # tie game
                        print('Your hand:', user_hand)
                        print('Dealers hand:', computer_hand)
                        print('The game was a tie. Both you and the dealer got Blackjack!')
                        # return to main menu
                    break
            break


# value of cards funciton
def value(x):
    # get rank of card
    card = x[0:1]
    # if card is an ace
    if card == 'A':
        # I coudln't figure out how to make ace worth either 1/11, so ace is autoamtically 11 (unless you are dealt 2, in which case
        # one of the aces will switch its value to 1
        card = 11
    # if card is a jack
    elif card == 'J':
        card = 10
    # if card is a wueen
    elif card == 'Q':
        card = 10
    # if card is a king
    elif card == 'K':
        card = 10
    card = int(card)
    return card


# deal function
def deal(card_deck):
    # get a random card
    card = random.choice(card_deck)
    # return the card
    return card

