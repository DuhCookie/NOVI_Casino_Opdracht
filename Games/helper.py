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