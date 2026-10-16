import random

def calculate_balance(win, balance, bet):
    if win == True:
        print(f'Gewonnen! Je wint €{int(bet) * 2}.')
        balance = balance + bet * 2
    else:
        print(f'Helaas... Je verliest je inzet van €{bet}.')
        balance -= bet

    return balance

def show_roulette_menu():
    print("Kies één van de volgende opties:")
    print("1. rood \n2. zwart \n3. even \n4. oneven \n0. stop")
    print()

def determine_win(roulette_choice, color, odd_even):
    if roulette_choice == '1' and color == 'rood':
        win = True
    elif roulette_choice == '2' and color == 'zwart':
        win = True
    elif roulette_choice == '3' and odd_even == 'even':
        win = True
    elif roulette_choice == '4' and odd_even == 'oneven':
        win = True
    else:
        win = False

    return win

def ask_for_bet(balance):
    """
    Prompts the player to place a bet and checks whether it is sufficient to start the game.
    :param balance:
    :return: bet
    """
    while True:
        bet = float(input(f'Huidig saldo = €{balance:.2f}\nHoeveel euro wil je inzetten?: '))

        if bet <= 0:
            print('Inzet is ongeldig. Kies een nieuw bedrag.')
            print()
            continue

        elif bet > balance:
            print('Onvoldoende saldo. Kies een nieuw bedrag.')
            print()
            continue

        else:
            return bet

def spin_wheel():
    spin = random.randint(0, 36)
    if spin == 0:
        color = 'groen'
        odd_even = 'geen'

    elif spin <= 18:
        if spin % 2 == 0:
            color = 'zwart'
            odd_even = 'even'
        else:
            color = 'rood'
            odd_even = 'oneven'

    else:
        if spin % 2 == 0:
            color = 'rood'
            odd_even = 'even'
        else:
            color = 'zwart'
            odd_even = 'oneven'

    print(f'De bal valt op {color} ({spin})')
    return color, odd_even

def play_roulette(balance):
    while True:
        if balance == 0:
            print('Je hebt onvoldoende saldo om verder te spelen.')
            break

        show_roulette_menu()

        roulette_choice = input("Kies je gok! (0 om te stoppen):")
        print()

        match roulette_choice:
            case '0':
                break
            case '1':
                print('Je hebt gekozen voor rood.')
            case '2':
                print('Je hebt gekozen voor zwart.')
            case '3':
                print('Je hebt gekozen voor even.')
            case '4':
                print('Je hebt gekozen voor oneven.')
            case _:
                print('Ongeldige keuze. Spel wordt opnieuw gestart...')
                print()
                continue

        bet = ask_for_bet(balance)
        color, odd_even = spin_wheel()
        win = determine_win(roulette_choice, color, odd_even)
        balance = calculate_balance(win, balance, bet)

    print(f"Eindsaldo: € {balance:.2f}")
    print('Bedankt voor het spelen!')
    return balance