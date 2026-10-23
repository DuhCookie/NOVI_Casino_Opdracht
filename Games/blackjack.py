
import random
from Games.helper import ask_for_bet

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def calculate_points(hand):
    """
    Calculates the total point value of all cards in the current hand.
    :param hand:
    :return:
    """
    total_points = 0
    aces = 0

    for card in hand:
        card_value = card[1]

        if card_value == 'A':
            total_points += 11
            aces += 1
        elif card_value == 'J' or card_value == 'Q' or card_value == 'K' or card_value == '1':
            total_points += 10
        else:
            total_points += int(card_value)

    while total_points > 21 and aces > 0:
        total_points -= 10
        aces -= 1

    return total_points

def check_results(points, hand):
    """
    Checks the player's total points to determine whether they can continue playing or have won/lost the round.
    :param points:
    :param hand:
    :return:
    """
    if points == 21 and len(hand) == 2:
        print('BLACKJACK')
        return 'win'
    elif points > 21:
        print('BUST!')
        return 'lose'
    else:
        return 'ongoing'

def create_deck(suits, ranks):
    """
    Creates a full deck and adds the card to the deck
    :param suits:
    :param ranks:
    :return: deck
    """
    deck = [suit + rank for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def show_hand(hide_card, player, dealer):
    """
    Displays the current hands and point totals for the player and dealer, with the option to hide one of the dealer's cards.
    :param hide_card: True or False
    :param player:
    :param dealer:
    :return:
    """
    if hide_card:
        print()
        print(f'Jouw hand: {' | '.join(player)}')
        print(f'Dealer toont: {dealer[0]} | ??')
        print(f'Jouw totaal: {calculate_points(player)}')
        print()
    else:
        print()
        print(f'Jouw hand: {' | '.join(player)}')
        print(f'Dealer toont: {' | '.join(dealer)}')
        print(f'Jouw totaal: {calculate_points(player)}')
        print(f'Totaal dealer: {calculate_points(dealer)}')
        print()

def draw_card(deck, hand):
    """
    Draws a card from the deck and adds it to the hand.
    :param deck:
    :param hand:
    :return: card
    """
    card = deck.pop(0)
    hand.append(card)
    return card

def player_turn(deck, player_hand, dealer_hand):
    """
    Handles the player's turn, allowing them to choose between drawing another card (Hit) or ending their turn (Stand).
    :param deck:
    :param player_hand:
    :param dealer_hand:
    :return:
    """
    while True:
        total_points = calculate_points(player_hand)
        show_hand(True, player_hand, dealer_hand)
        result = check_results(total_points, player_hand)

        if result == 'win' or result == 'lose':
            return result
        else:
            player_choice = input('Wat wil je doen? \n1. Hit \n2. Stand \n\nNummer van keuze: ')
            if player_choice == '1':
                print(f'Jij trekt: {draw_card(deck, player_hand)}')
                continue

            elif player_choice == '2':
                break

            else:
                print('Ongeldige keuze. Kies opnieuw.')
                continue

def dealer_turn(deck, player_hand, dealer_hand, result):
    """
    Handles the dealer's turn.
    :param deck:
    :param player_hand:
    :param dealer_hand:
    :param result:
    :return:
    """
    if result == 'win' or result == 'lose':
        return

    show_hand(False, player_hand, dealer_hand)
    points = calculate_points(dealer_hand)

    while points < 17:
        print('De dealer trekt nog een kaart...')
        print(f'Dealer trekt: {draw_card(deck, dealer_hand)}')
        points = calculate_points(dealer_hand)
        show_hand(False, player_hand, dealer_hand)

def determine_win(player, dealer, bet):
    """
    Compares the player's and dealer's hands to determine the outcome of the round.
    :param player:
    :param dealer:
    :param bet:
    :return:
    """
    total_player = calculate_points(player)
    total_dealer = calculate_points(dealer)

    if total_dealer > 21:
        print(f'Gewonnen!!! Je wint €{(bet * 2):.2f}!')
        result = 'jackpot'
    elif total_player == total_dealer:
        result = 'tie'
        print(f'Gelijk spel! Je wint je inzet van €{bet} terug.')
    elif total_player > 21 or total_player < total_dealer:
        result = 'lose'
        print(f'Helaas! Je verliest je inzet van €{bet}...')
    else:
        result = 'win'
        print(f'Gewonnen!!! Je wint €{(bet * 1.5):.2f}!')
    print()
    return result

def calculate_balance(result, bet, balance):
    """
    Updates the player's balance based on the outcome of the round and the amount wagered.
    :param result:
    :param bet:
    :param balance:
    :return:
    """
    if result == 'win':
        balance += (bet * 1.5)
    elif result == 'jackpot':
        balance += (bet * 2)
    elif result == 'lose':
        balance -= bet
    return balance

def play_blackjack(balance):
    """
    Plays a complete round of Blackjack.
    :param balance:
    :return:
    """
    while True:
        blackjack_round = input('Wil je een ronde blackjack spelen? J/N: ').capitalize()
        if blackjack_round == 'N':
            break
        elif blackjack_round == 'J':
            pass
        else:
            print('Ongeldig antwoord... Probeer opnieuw.')
            continue

        bet = ask_for_bet(balance)
        deck = create_deck(SUITS, RANKS)

        player_hand = []
        dealer_hand = []

        for cards in range(2):
            draw_card(deck, player_hand)
            draw_card(deck, dealer_hand)

        result = player_turn(deck, player_hand, dealer_hand)
        dealer_turn(deck, player_hand, dealer_hand, result)
        result = determine_win(player_hand, dealer_hand, bet)
        balance = calculate_balance(result, bet, balance)

    print(f"Eindsaldo: € {balance:.2f}")
    print('Bedankt voor het spelen!')
    return balance



