# Cvičení 1 – Dvě kostky
# Doplň kód pod zadání a soubor spusť (Run).

# Hoď dvěma kostkami (každá má čísla 1 až 6) a vypiš obě čísla
#    i jejich součet. Použij randrange z modulu random.
#    Ukázka výstupu:
#
#    Padlo 3 a 5, dohromady 8.


import random

throw = random.randrange(1,7)

first_number = random.randrange(1,7)
second_number = random.randrange(1,7)

print(f"\n First number:", first_number, "\n Second number:" , second_number ,"\n Together:", first_number + second_number)