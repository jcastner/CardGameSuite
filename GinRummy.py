# CS021
# Couby Ouattara
# Final Project: Gin Rummy


import random

SPADES = '\u2660'
CLUBS = '\u2663'
DIAMONDS = '\u2666'
HEARTS = '\u2665'

ACE = "A"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
SEVEN = "7"
EIGHT = "8"
NINE = "9"
TEN = "10"
KING = "K"
QUEEN = "Q"
JACK = "J"

player_1 = []
player_2 = []
discard_pile = []

card_deck = []

MELD_LEN = 3

ranks = (CLUBS, HEARTS, DIAMONDS, SPADES)
suits = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


def main():
    deck_cards(ranks, suits)
    deal(player_1, player_2, discard_pile, card_deck)

    player1_name = input("Enter player 1 name: ")
    player2_name = input("Enter player 2 name: ")

    card_deck_len = len(card_deck)

    player1_score_count = 0
    player2_score_count = 0

    knock_goGin = input("Do player 1 or player 2 want to knock or go gin?, enter play to continue playing: ")

    while knock_goGin == "play" and card_deck_len > 2 and player1_score_count < 100 and player2_score_count < 100:

        print("Player 1 cards: ", player_1)
        print("Player 2 cards: ", player_2)

        print("***************************IT IS PLAYER 1 TURN**********************************")

        print("This is the upcard", discard_pile)

        first_play = input(
            "Player 1 may either draw the upcard or pass the turn. Enter D to draw the upcard or enter P to pass turn:")

        if first_play == "D":

            player_1.append(discard_pile[0])
            discard_pile.remove(discard_pile[0])

            print("These are your cards now: ", player_1)

            draw_card = int(input(
                "which card would you like discard to the the discard pile? Enter a number from 0 to 10 to select one card from your cards: "))

            discard_pile.append(player_1[draw_card])
            player_1.remove(player_1[draw_card])

            print("***************************IT IS PLAYER 2 TURN**********************************")

            print("This is the dicarded card:", discard_pile)

            answer = input("Enter D to draw the discarded card or enter P to draw a random card from the stock pile: ")

            if answer == "D":

                player_2.append(discard_pile[0])
                discard_pile.remove(discard_pile[0])

                print("These are your cards now: ", player_2)

                draw_card = int(input(
                    "which card would you like discard to the discard pile? Enter a number from 0 to 10 to select one card from your cards:"))

                discard_pile.append(player_2[draw_card])
                player_2.remove(player_2[draw_card])

            elif answer == "P":

                deck_len = int(len(card_deck))

                num = random.randint(0, deck_len)

                player_2.append(card_deck[num])
                card_deck.remove(card_deck[num])

                print("Player, A random card has been added to your cards")
                print("player 2 these are your cards: ", player_2)

                draw_card = int(input(
                    "Player 2: which card would you like discard to the the discard pile? Enter a number from 0 to 10 to select one card from your cards:"))

                discard_pile.append(player_2[draw_card])
                player_2.remove(player_2[draw_card])



        elif first_play == "P":

            print("***************************IT IS PLAYER 2 TURN**********************************")

            start_play = input(
                "Player 2 may either draw the upcard or pass the turn. Enter: D to draw the upcard or enter P to pass turn:")

            if start_play == "D":

                player_2.append(discard_pile[0])
                discard_pile.remove(discard_pile[0])

                print("These are your cards now: ", player_2)

                draw_card = int(input(
                    "which card would you like discard to the the discard pile? Enter a number from 0 to 10 to select one card from your cards:"))

                discard_pile.append(player_2[draw_card])
                player_2.remove(player_2[draw_card])

                print("***************************IT IS PLAYER 1 TURN**********************************")

                print("This is the dicarded card:", discard_pile)
                Answer = input(
                    "Player 1 may Enter D to draw the discarded card or enter P to draw a random card from the stock pile: ")

                if Answer == "D":

                    player_1.append(discard_pile[0])
                    discard_pile.remove(discard_pile[0])

                    print("These are your cards now: ", player_1)

                    draw_card = int(input(
                        "Player 1: which card would you like discard to the the discard pile? Enter a number from 0 to 11 to select one card from your cards:"))

                    discard_pile.append(player_1[draw_card])
                    player_1.remove(player_1[draw_card])

                elif Answer == "P":

                    deck_len = int(len(card_deck))

                    num = random.randint(0, deck_len)

                    player_1.append(card_deck[num])
                    card_deck.remove(card_deck[num])

                    print("Player, A random card has been added to your cards")
                    print("player 1 these are your cards: ", player_1)

                    draw_card = int(input(
                        "Player 1: which card would you like discard to the the discard pile? Enter a number from 0 to 11 to select one card from your cards:"))

                    discard_pile.append(player_1[draw_card])
                    player_1.remove(player_2[draw_card])

                elif start_play == "P":

                    print("***************************IT IS PLAYER 1 TURN**********************************")

                    deck_len = int(len(card_deck))

                    num = random.randint(0, deck_len)

                    player_1.append(card_deck[num])
                    card_deck.remove(card_deck[num])

                    print("Player, A random card has been added to your cards")
                    print("player 1 these are your cards: ", player_1)

                    draw_card = int(input(
                        "Player 1: which card would you like discard to the the discard pile? Enter a number from 0 to 10 to select one card from your cards:"))

                    discard_pile.append(player_1[draw_card])
                    player_1.remove(player_1[draw_card])

                    print("***************************IT IS PLAYER 2 TURN**********************************")

                    print("This is the dicarded card:", discard_pile)
                    Answer = input(
                        "Player 1 may Enter D to draw the discarded card or enter P to draw a random card from the stock pile: ")

                    if Answer == "D":

                        player_2.append(discard_pile[0])
                        discard_pile.remove(discard_pile[0])

                        print("These are your cards now: ", player_2)

                        draw_card = int(input(
                            "Player 1: which card would you like discard to the the discard pile? Enter a number from 0 to 10 to select one card from your cards:"))

                        discard_pile.append(player_2[draw_card])
                        player_2.remove(player_2[draw_card])

                    elif Answer == "P":

                        deck_len = int(len(card_deck))

                        num = random.randint(0, deck_len)

                        player_2.append(card_deck[num])
                        card_deck.remove(card_deck[num])

                        print("Player, A random card has been added to your cards")
                        print("player 2 these are your cards: ", player_2)

                        draw_card = int(input(
                            "Player 2: which card would you like discard to the the discard pile? Enter a number from 0 to 10 to select one card from your cards:"))

                        discard_pile.append(player_2[draw_card])
                        player_2.remove(player_2[draw_card])

        card_deck_len = len(card_deck)

        player1_deadwoods = score(player_1)
        player2_deadwoods = score(player_2)

        if player1_deadwoods < player2_deadwoods:

            player1_score = player2_deadwoods - player1_deadwoods

            player2_score = 0

            player1_score_count = + player1_score
            player2_score_count = + player2_score



        elif player2_deadwoods < player1_deadwoods:

            player1_score = player1_deadwoods - player2_deadwoods

            player2_score = 0

            player1_score_count = + player1_score
            player2_score_count = + player2_score



        elif player1_deadwoods == player2_deadwoods:

            player1_score = 0

            player2_score = 0

            player1_score_count = + player1_score
            player2_score_count = + player2_score

        knock_goGin = input("Does player 1 or player 2 want to knock or go gin?, enter play to continue playing: ")

    if player1_score_count < player2_score_count:

        print("*******GAME OVER!***********")

        print(player1_name, "YOU HAVE WON CONGRATULATIONS!!!")

    elif player2_score_count < player1_score_count:

        print("*******GAME OVER!***********")

        print(player2_name, "YOU HAVE WON CONGRATULATIONS!!!")

    else:

        print("ITS A TIE GAME!")


def deck_cards(ranks, suits):
    card_value = 1
    for x in ranks:
        for y in suits:
            card_deck.append([x, y])
    random.shuffle(card_deck)


def deal(player_1, player_2, discard_pile, card_deck):
    for card in range(10):
        player_1.append(card_deck[0])
        card_deck.remove(card_deck[0])
        player_2.append(card_deck[0])
        card_deck.remove(card_deck[0])

    discard_pile.append(card_deck[0])
    card_deck.remove(card_deck[0])


def score(player):
    ace = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    jack = []
    queen = []
    king = []

    len_ace = len(ace)
    len_two = len(two)
    len_three = len(three)
    len_four = len(four)
    len_five = len(five)
    len_six = len(six)
    len_seven = len(seven)
    len_eight = len(eight)
    len_nine = len(nine)
    len_ten = len(ten)
    len_jack = len(jack)
    len_queen = len(queen)
    len_king = len(king)

    spades = []
    hearts = []
    diamonds = []
    clubs = []

    len_spades = len(spades)
    len_hearts = len(hearts)
    len_diamond = len(diamonds)
    len_clubs = len(clubs)

    count_num = []

    count = 0

    for card in player:

        get_rank = card[1]

        if get_rank == ACE:
            ace.append(get_rank)

        elif get_rank == TWO:
            two.append(get_rank)

        elif get_rank == THREE:
            three.append(get_rank)

        elif get_rank == FOUR:
            four.append(get_rank)

        elif get_rank == FIVE:
            five.append(get_rank)

        elif get_rank == SIX:
            six.append(get_rank)

        elif get_rank == SEVEN:
            seven.append(get_rank)

        elif get_rank == EIGHT:
            eight.append(get_rank)

        elif get_rank == NINE:
            nine.append(get_rank)

        elif get_rank == TEN:
            ten.append(get_rank)

        elif get_rank == JACK:
            jack.append(get_rank)

        elif get_rank == QUEEN:
            queen.append(get_rank)

        elif get_rank == KING:
            king.append(get_rank)

    for Ace in ace:

        if len_ace >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == ACE:
                    player.remove(card)

    for Two in two:

        if len_two >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == TWO:
                    player.remove(card)

    for Three in three:

        if len_three >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == THREE:
                    player.remove(card)

    for Four in four:

        if len_four >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == FOUR:
                    player.remove(card)

    for Five in five:

        if len_five >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == FIVE:
                    player.remove(card)

    for Six in six:

        if len_six >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == SIX:
                    player.remove(card)

    for Seven in seven:

        if len_seven >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == SEVEN:
                    player.remove(card)

    for Eight in eight:

        if len_eight >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == EIGHT:
                    player.remove(card)

    for Nine in nine:

        if len_nine >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == NINE:
                    player.remove(card)

    for Ten in ten:

        if len_ten >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == TEN:
                    player.remove(card)

    for King in king:

        if len_king >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == KING:
                    player.remove(card)

    for Jack in jack:

        if len_jack >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == JACK:
                    player.remove(card)

    for Queen in ace:

        if len_queen >= MELD_LEN:

            for card in player:

                get_rank = card[1]

                if get_rank == QUEEN:
                    player.remove(card)

    for card in player:

        get_suit = card[0]

        if get_suit == SPADES:
            spades.append(get_suit)

        elif get_suit == HEARTS:
            hearts.append(get_suit)

        elif get_suit == CLUBS:
            clubs.append(get_suit)

        elif get_suit == DIAMONDS:
            diamonds.append(get_suit)

    for Spades in spades:

        if len_spades >= MELD_LEN:

            for card in player:

                get_suit = card[0]

                if get_suit == SPADES:
                    player.remove(card)

    for Hearts in hearts:

        if len_hearts >= MELD_LEN:

            for card in player:

                get_suit = card[0]

                if get_suit == HEARTS:
                    player.remove(card)

    for Diamonds in diamonds:

        if len_diamond >= MELD_LEN:

            for card in player:

                get_suit = card[0]

                if get_suit == DIAMONDS:
                    player.remove(card)

    for Clubs in clubs:

        if len_clubs >= MELD_LEN:

            for card in player:

                get_suit = card[0]

                if get_suit == CLUBS:
                    player.remove(card)

    for card in player:

        get_rank = card[1]

        if get_rank == ACE:
            count_num.append(1)


        elif get_rank == TWO:
            count_num.append(2)

        elif get_rank == THREE:

            count_num.append(3)

        elif get_rank == FOUR:
            count_num.append(4)


        elif get_rank == FIVE:
            count_num.append(5)


        elif get_rank == SIX:
            count_num.append(6)

        elif get_rank == SEVEN:
            count_num.append(7)


        elif get_rank == EIGHT:
            count_num.append(8)


        elif get_rank == NINE:
            count_num.append(9)


        elif get_rank == TEN:
            count_num.append(10)

        elif get_rank == JACK:
            count_num.append(10)


        elif get_rank == QUEEN:
            count_num.append(10)


        elif get_rank == KING:
            count_num.append(10)

    for num in count_num:
        count += num

    return count










