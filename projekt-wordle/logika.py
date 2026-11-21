# Wordle – LOGIKA
#
# Sem piš funkce s pravidly hry. Dostanou data a výsledek vrátí (return).
# Nepatří sem žádný input() ani print(), ty piš do wordle.py.
# Díky tomu půjdou funkce z tohohle souboru testovat.
#
# Začni krokem 1: cviceni/01_jeden_pokus.md

DELKA_SLOVA = 5
POCET_POKUSU = 6
# hadane = "kabát"
# tajne = "kočka"

def vyhodnot(hadane, tajne):
    # pozice = ["spravne", "jinde", "neni"]
    pozice = []
    for i in range (DELKA_SLOVA):
        if hadane[i] == tajne[i]:
            pozice.append("spravne")
        elif hadane[i] in tajne[:]:
            pozice.append("jinde")
        else:
            pozice.append("neni")
            
    return(pozice)
# vyhodnot("kabát", "kočka")