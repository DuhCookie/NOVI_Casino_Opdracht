import datetime

PRICE_ENTREE = 14.99
PRICE_WARDROBE = 1.95
PRICE_PARKING = 9.99
FIXED_COSTS = PRICE_ENTREE + PRICE_WARDROBE + PRICE_PARKING
MIN_AGE = 18

salution = ""
first_name = input("Wat is je voornaam?\n Voornaam: ").capitalize()
surname = input("Wat is je achternaam?\n Achternaam: ").capitalize()

birth_date = input("Wat is je geboortedatum?\n (dd-mm-yyyy): ")
current_year = datetime.datetime.now().year
birth_day, birth_month, birth_year = birth_date.split("-")


if current_year - int(birth_year) < MIN_AGE:
    print()
    print("Helaas ben je te jong om deel te nemen aan Casino de Sluwe Kat.")
    print("Je moet minstens 18 jaar oud zijn.")
    print()
    print("Bedankt voor je begrip!")
    exit(1)

gender = input("Wat is je geslacht?\n Man / Vrouw / Anders: ").lower()
start_budget = float(input("Wat is je startbudget in euro's?\n Startbudget: "))
balance = start_budget - FIXED_COSTS
bet = 0
round_number = 1

balance_conclusion = ""

if gender == "man":
    salution = f"meneer {surname}"

elif gender == "vrouw":
    salution = f"mevrouw {surname}"

else:
    salution = f"{first_name} {surname}"

if balance >= 0:
    balance_conclusion = "Je hebt voldoende budget voor toegang tot het casino."

else:
    balance_conclusion = "Je hebt onvoldoende budget voor toegang tot het casino."

print()
print("-" * 20)
print("Casino de Sluwe Kat")
print("-" * 20)
print(f"Welkom, {salution}!")
print()
print(f"Startbudget:    € {start_budget:.2f}")
print(f"Vaste kosten:   € {FIXED_COSTS:.2f}")
print(f"Saldo:          € {balance:.2f}")
print()
print(balance_conclusion)

while True:
    print("Kies één van de volgende opties:")
    print("1. rood \n2. zwart \n3. even \n4. oneven \n0. stop")
    print()
    roulette_choice = input("Kies je gok! (0 om te stoppen):")
    print()

    spin = (round_number * 7) % 37
    round_number += 1

    if roulette_choice == '0':
        print('Bedankt voor het spelen!')
        break

    else:
        match roulette_choice:
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

        # Check inzet
        bet = float(input(f'Huidig saldo = €{balance}\nHoeveel euro wil je inzetten?: '))

        if bet <= 0:
            print('Inzet is ongeldig. Spel wordt opnieuw gestart...')
            print()
            continue
        elif bet > balance:
            print('Onvoldoende saldo. Spel wordt opnieuw gestart...')
            print()
            continue
        else:
            balance -= bet

        # Check kleur
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
                color = 'rood'
                odd_even = 'oneven'

        # Check uitslag
        win = False
        if roulette_choice == '1' and color == 'rood':
            win = True
        elif roulette_choice == '2' and color == 'zwart':
            win = True
        elif roulette_choice == '3' and odd_even == 'even':
            win = True
        elif roulette_choice == '4' and odd_even == 'oneven':
            win = True

        # Print uitslag
        print(f'De bal valt op {color} ({spin})')

        if win == True:
            print(f'Gewonnen! Je wint €{bet}.')
            balance = balance + bet * 2
        else:
            print(f'Helaas... Je verliest je inzet van €{bet}.')

        print()
        print(f'Huidig saldo = €{balance:.2f}')
        print()
        continue




