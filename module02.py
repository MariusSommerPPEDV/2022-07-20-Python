# Funktionen & Kontrollstrukturen

# Definieren von Funktionen
# def identifier(parameter1, parameter2,....):

# Auf zu kurze Funktionsnamen verzichten und auch unbekannte Abkürzungen vermeiden
def gP(n):
    print("Hallo ", n)


# Klare Benennung, die auf dem ersten Blick die Funktion erklärt
def greet_person(name):
    print("Hello", name)


def greet_world():
    print("Hello World!")


# Aufrufen einer Funktion:
greet_person("Max Mustermann")
greet_person("Max Mustermann")


# Funktionen können auch Werte zurückgeben
# dafür wird das keyword return benutzt
def add_numbers(number1, number2):
    return number1 + number2


resultOne = add_numbers(55, 66)
print(resultOne)

# Variablen können auch als Parameter agieren

resultOne = add_numbers(resultOne, resultOne)

print(resultOne)

# In Python können auch mehrere Werte zurückgegeben werden


def return_numbers(number1, number2, number3):
    print(resultOne)
    return number1, number2, number3


print(return_numbers(1, 4, 8))

# Können auch mehreren Variablen zugewiesen werden

resultTwo, resultThree, resultFour = return_numbers(1, 4, 8)

print(resultTwo)
print(resultThree)
print(resultFour)

# resultTwo, resultThree = return_numbers(12, 5, 8)
# Es müssen genau so viele Variable wie return Werte angegeben werden
# Ausnahme: Wenn ich die Werte einer einzigen Variable zuweise, wird diese zu einem Tupel

resultTwo = return_numbers(12, 4, 8)

# Scopes in Python:
# global scope, alles was auf oberster Ebene definiert wurde
# Kann im gesamten Skript aufgerufen werden

# local scope
# Variablen sind local, sobald sie eingerückt definiert wurden


def scope_demonstration():
    print(resultOne)
    greet_world()
    x = 20
    y = 25
    def inner_function():  # lokal definierte Funktion, also nur innerhalb der scope_demonstration aufrufbar
        x = 15
        print(x)  # Hier wird x 15 sein, da inner_function erst im eigenem lokalen Scope nach der variable sucht,
        # bevor er die äußeren Scopes durchsucht
        print(y)  # Kann aufgerufen werden, da inner_function alle Variablen kennt, die scope_demonstration definiert
    inner_function()
    print(x)  # Hier wird x 20 sein


scope_demonstration()

# Übung 1 - Funktionen:
# Schreibe eine Funktion, die zwei Zahlen als Parameter erhält, die Zahlen dann jeweils verdoppelt und beide zurückgibt


def double_numbers(number1, number2):
    number1 = number1 * 2
    number2 = number2 * 2
    return number1 * 2, number2 * 2


resultFive = double_numbers(200, 100)  # resultFive wird zu einem Tupel (400, 200)
num1, num2 = double_numbers(200, 100)  # num1 wird zu 400 und num2 wird zu 200

print("resultFive:", resultFive)
print("num1:", num1, "num2:", num2)


