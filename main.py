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



