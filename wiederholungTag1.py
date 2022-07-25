# string - Textketten
# int - Ganzzahlen
# float - Kommazahlen
# bool - Wahr/Falsch

# Collections
# list - index
# dictionaries - keys
# tuple - index
# sets  - nicht geordnet, kein index

# Funktionen

# def functionIdentifier():
#       eingerückt gehts weiter
#       return gibt Werte zurück

def return_one():
    return 1


def return_multiple():
    return 1, 2, 3


x = return_multiple()  # x ist jetzt ein Tuple

x, y, z = return_multiple()  # x = 1, y = 2, z = 3

# if, elif, else

#  Wdh. Übung:
# Erstelle eine Funktion, die eine Zahl als Parameter übergeben bekommt und prüft, ob die Zahl gerade oder ungerade ist
# Die Konsole soll uns dann ausgeben, ob die Zahl gerade ist oder ungerade


def is_even(number):
    if number % 2 == 0:
        print(number, "ist gerade.")
    else:
        print(number, "ist ungerade.")


is_even(45)
is_even(46)
