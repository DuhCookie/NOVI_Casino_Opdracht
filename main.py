import datetime

PRIJS_TOEGANGSTICKET = 14.99
PRIJS_GARDEROBE = 1.95
PRIJS_PARKEREN = 9.99
VASTE_KOSTEN = PRIJS_TOEGANGSTICKET + PRIJS_GARDEROBE + PRIJS_PARKEREN
MIN_LEEFTIJD = 18

aanhef = ""
voornaam = input("Wat is je voornaam?\n Voornaam: ").capitalize()
achternaam = input("Wat is je achternaam?\n Achternaam: ").capitalize()

geboortedatum = input("Wat is je geboortedatum?\n (dd-mm-yyyy): ")
huidig_jaar = datetime.datetime.now().year
geboorte_dag, geboorte_maand, geboorte_jaar = geboortedatum.split("-")


if huidig_jaar - int(geboorte_jaar) < MIN_LEEFTIJD:
    print()
    print("Helaas ben je te jong om deel te nemen aan Casino de Sluwe Kat.")
    print("Je moet minstens 18 jaar oud zijn.")
    print()
    print("Bedankt voor je begrip!")
    exit(1)

geslacht = input("Wat is je geslacht?\n Man / Vrouw / Anders: ").lower()
startbudget = float(input("Wat is je startbudget in euro's?\n Startbudget: "))
saldo = startbudget - VASTE_KOSTEN
inzet = 0
round_number = 1

conclusie_saldo = ""

if geslacht == "man":
    aanhef = f"meneer {achternaam}"

elif geslacht == "vrouw":
    aanhef = f"mevrouw {achternaam}"

else:
    aanhef = f"{voornaam} {achternaam}"

if saldo >= 0:
    conclusie_saldo = "Je hebt voldoende budget voor toegang tot het casino."

else:
    conclusie_saldo = "Je hebt onvoldoende budget voor toegang tot het casino."

print()
print("-" * 20)
print("Casino de Sluwe Kat")
print("-" * 20)
print(f"Welkom, {aanhef}!")
print()
print(f"Startbudget:    € {startbudget:.2f}")
print(f"Vaste kosten:   € {VASTE_KOSTEN:.2f}")
print(f"Saldo:          € {saldo:.2f}")
print()
print(conclusie_saldo)

while True:
    print("Kies één van de volgende opties:")
    print("1. rood \n2. zwart \n3. even \n4. oneven \n0. stop")
    print()
    roulette_keuze = input("Kies je gok! (0 om te stoppen):")
    print()

    spin = (round_number * 7) % 37
    round_number += 1

    if roulette_keuze == '0':
        print('Bedankt voor het spelen!')
        break

    else:
        match roulette_keuze:
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
        inzet = float(input(f'Huidig saldo = €{saldo}\nHoeveel euro wil je inzetten?: '))

        if inzet <= 0:
            print('Inzet is ongeldig. Spel wordt opnieuw gestart...')
            print()
            continue
        elif inzet > saldo:
            print('Onvoldoende saldo. Spel wordt opnieuw gestart...')
            print()
            continue
        else:
            saldo -= inzet

        # Check kleur
        if spin == 0:
            kleur = 'groen'
            even_oneven = 'geen'

        elif spin <= 18:
            if spin % 2 == 0:
                kleur = 'zwart'
                even_oneven = 'even'
            else:
                kleur = 'rood'
                even_oneven = 'oneven'

        else:
            if spin % 2 == 0:
                kleur = 'rood'
                even_oneven = 'even'
            else:
                kleur = 'rood'
                even_oneven = 'oneven'

        # Check uitslag
        win = False
        if roulette_keuze == '1' and kleur == 'rood':
            win = True
        elif roulette_keuze == '2' and kleur == 'zwart':
            win = True
        elif roulette_keuze == '3' and even_oneven == 'even':
            win = True
        elif roulette_keuze == '4' and even_oneven == 'oneven':
            win = True

        # Print uitslag
        print(f'De bal valt op {kleur} ({spin})')

        if win == True:
            print(f'Gewonnen! Je wint €{inzet}.')
            saldo = saldo + inzet * 2
        else:
            print(f'Helaas... Je verliest je inzet van €{inzet}.')

        print()
        print(f'Huidig saldo = €{saldo:.2f}')
        print()
        continue




