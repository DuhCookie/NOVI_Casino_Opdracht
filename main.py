import datetime
from Games.roulette import play_roulette
from Games.fruitmachine import play_fruitmachine

PRICE_ENTREE = 14.99
PRICE_WARDROBE = 1.95
PRICE_PARKING = 9.99
FIXED_COSTS = PRICE_ENTREE + PRICE_WARDROBE + PRICE_PARKING
MIN_AGE = 18

def calculate_age(birth_date):
    current_year = datetime.datetime.now().year
    birth_day, birth_month, birth_year = birth_date.split("-")
    return current_year - int(birth_year)

def check_age(birth_date):
    if calculate_age(birth_date) < MIN_AGE:
        print()
        print("Helaas ben je te jong om deel te nemen aan Casino de Sluwe Kat.")
        print("Je moet minstens 18 jaar oud zijn.")
        print()
        print("Bedankt voor je begrip!")
        exit(1)
    else:
        return birth_date

def determine_salutation(first_name, surname, gender):
    if gender == "man":
        salutation = f"meneer {surname}"

    elif gender == "vrouw":
        salutation = f"mevrouw {surname}"

    else:
        salutation = f"{first_name} {surname}"

    return salutation

def show_welcome_message(start_budget, balance, salutation):
    print()
    print("-" * 20)
    print("Casino de Sluwe Kat")
    print("-" * 20)
    print(f"Welkom, {salutation}!")
    print()
    print(f"Startbudget:    € {start_budget:.2f}")
    print(f"Vaste kosten:   € {FIXED_COSTS:.2f}")
    print(f"Saldo:          € {balance:.2f}")
    print()

    if balance <= 0:
        print("Je hebt onvoldoende budget voor toegang tot het casino.")
        exit(1)
    else:
        print("Je hebt voldoende budget voor toegang tot het casino.")

def menu_header(title):
    print()
    print("-" * 10)
    print(title)
    print("-" * 10)
    print()

def show_main_menu():
    menu_header('HOOFDMENU')
    print("1. Spellen \n2. Saldo \n3. Account \n0. Stop")
    print()

def show_game_menu():
    menu_header('SPELLEN')
    print("1. Fruitmachine \n2. Roulette \n0. Terug")
    print()

def show_balance(balance):
    menu_header('SALDO')
    print(f"Huidig saldo: € {balance:.2f}")
    print()
    print("0. Terug")
    print()

def show_account(first_name, surname, gender, birth_date):
    menu_header('ACCOUNT')
    print(f'Naam: {first_name} {surname}')
    print(f'Geslacht: {gender.capitalize()}')
    print(f'Geboortedatum: {birth_date}')
    print(f'Leeftijd: {calculate_age(birth_date)}')
    print()
    print("0. Terug")
    print()

def main():
    first_name = input("Wat is je voornaam?\n Voornaam: ").capitalize()
    surname = input("Wat is je achternaam?\n Achternaam: ").capitalize()
    birth_date = check_age(input("Wat is je geboortedatum?\n (dd-mm-yyyy): "))
    gender = input("Wat is je geslacht?\n Man / Vrouw / Anders: ").lower()
    start_budget = float(input("Wat is je startbudget in euro's?\n Startbudget: "))

    salutation = determine_salutation(first_name, surname, gender)

    balance = start_budget - FIXED_COSTS
    show_welcome_message(start_budget, balance, salutation)

    while True:
        show_main_menu()
        menu_choice = input("Voer het nummer van je keuze in: ")

        match menu_choice:
            case '1':
                show_game_menu()
                game_choice = input('Voer het nummer van je keuze in: ')

                if game_choice == '1':
                    menu_header('FRUITMACHINE')
                    balance = play_fruitmachine(balance)

                elif game_choice == '2':
                    menu_header('ROULETTE')
                    balance = play_roulette(balance)

                elif game_choice == '0':
                    continue

                else:
                    print('Ongeldige keuze')
                    continue

            case '2':
                show_balance(balance)
                balance_choice = input('Voer het nummer van je keuze in: ')

                if balance_choice == '0':
                    continue

            case '3':
                show_account(first_name, surname, gender, birth_date)
                account_choice = input('Voer het nummer van je keuze in: ')

                if account_choice == '0':
                    continue

            case '0':
                print()
                print('Bedankt voor het spelen!')
                break
            case _:
                print()
                print('Ongeldige keuze.')
                continue

    print(f"Eindsaldo: € {balance:.2f}")

main()




