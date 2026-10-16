import random
from Games.roulette import ask_for_bet

def generate_slots():
    """
    Generates random numbers for three slots.
    :return: a number for slot 1, 2 and 3
    """
    slot_1 = random.randint(1, 3)
    slot_2 = random.randint(1, 3)
    slot_3 = random.randint(1, 3)

    return slot_1, slot_2, slot_3

def print_slots(slots):
    """
    Displays the slot's image.
    :param slots:
    """
    print('Het slotmachine draait...')

    for slot in slots:
        if slot == 1:
            print('🍎')
        elif slot == 2:
            print('🍐')
        else:
            print('🍌')

def determine_win(slot_1, slot_2, slot_3, bet):
    """
    Determines whether the player has won based on the slot results and prints the result.
    :param slot_1:
    :param slot_2:
    :param slot_3:
    :param bet:
    """
    if slot_1 == slot_2 == slot_3:
        print(f'Jackpot!!! Je wint €{(bet * 3):.2f}!')
        return 'Jackpot'

    elif slot_1 == slot_2 or slot_2 == slot_3 or slot_3 == slot_1:
        print(f'Je hebt gewonnen! Je wint €{bet:.2f}!')
        return 'Win'

    else:
        print(f'Helaas! Je verliest je inzet van €{bet}...')
        return 'Lose'

def calculate_payout(win, bet, balance):
    """
    Displays the player's winnings and calculates their updated balance.
    :param win:
    :param bet:
    :param balance:
    :return:
    """
    if win == 'Jackpot':
        balance += (bet * 3)
    elif win == 'Win':
        balance += bet
    else:
        balance -= bet

    return balance

def play_fruitmachine(balance):
    """"
    Runs the fruit machine game.
    """
    while True:
        fruitmachine_spin = input('Wil je aan de fruitmachine draaien? J/N: ').capitalize()
        if fruitmachine_spin == 'N':
            break
        elif fruitmachine_spin == 'J':
            pass
        else:
            print('Ongeldig antwoord... Probeer opnieuw.')
            continue

        bet = ask_for_bet(balance)
        slot_1, slot_2, slot_3 = generate_slots()
        slots = [slot_1, slot_2, slot_3]
        print_slots(slots)
        win = determine_win(slot_1, slot_2, slot_3, bet)
        balance = calculate_payout(win, bet, balance)

    print(f"Eindsaldo: € {balance:.2f}")
    print('Bedankt voor het spelen!')
    return balance