# Wordle – HRA
#
# Tenhle soubor spouštíš (Run). Ptá se hráče na slova, volá funkce
# z logika.py a vypisuje výsledky. Patří sem všechno s input() a print().
#
# Začni krokem 1: cviceni/01_jeden_pokus.md

import logika

ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}

print("Wordle")
print(f"Hádáš slovo o {logika.DELKA_SLOVA} písmenech a máš {logika.POCET_POKUSU} pokusů.")

def vypis_pokus(hadane, vysledek):
    pozice = logika.vyhodnot(hadane, vysledek)
    # ZNACKY = []
    # pismena = []
    for i in pozice:
        print(ZNACKY[i], end= " ")

vypis_pokus("kabat","kočka")
print()

