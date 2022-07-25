# Userinput und Casting

# Input vom User abfragen:
# In Python mittels input() möglich
# Input akzeptiert einen Parameter, das ist der Text der angezeigt wird

def greet_person():
    name = input("Wie ist dein Name?\n")
    # \n Erzeugt einen Zeilenumbruch
    # Name erhält den Wert, den der User in der Konsole eingibt
    print(f"Hallo {name}")


# greet_person()


# Standardmäßig gibt input() immer einen string zurück
# Bei calc müssen wir also unseren Typen verändern
# Dafür nutzen wir das casting

def calc():
    print("Welche Zahlen sollen addiert werden?")
    numOne = input("1. Zahl: ")
    numTwo = input("2. Zahl: ")
    # Hier wird nicht konvertiert
    print(numOne + numTwo)  # Die beiden Strings werden einfach aneinander gereiht


# calc()
print("Marius" + "Sommer")


def calc_casting():
    print("Welche Zahlen sollen addiert werden?")
    numOne = input("1. Zahl: ")  # string
    numTwo = input("2. Zahl: ")  # string
    numOne = int(numOne)  # string wird in int konvertiert
    numTwo = int(numTwo)  # string wird in int konvertiert
    print(numOne + numTwo)


# calc_casting()


# Übung 1 Input:
# Passe die calc_casting() Funktion so an, dass nur gecasted wird, wenn Zahlen übergeben wurden
# Falls nicht soll in der Konsole ausgegeben werden, dass nur Zahlen akzeptiert werden

# def calc_loop():
#     print("Welche Zahlen sollen addiert werden?")
#     numOne = input("1. Zahl: ")
#     while not numOne.isnumeric():
#         print("Es muss eine Zahl übergeben werden")
#         numOne = input("1. Zahl: ")  # string
#     numTwo = input("2. Zahl: ")  # string
#     while not numTwo.isnumeric():
#         print("Es muss eine Zahl übergeben werden")
#         numTwo = input("2. Zahl: ")
#     print(int(numOne) + int(numTwo))

# Optimale Lösung mit assignment expressions
def calc_loop():
    print("Welche Zahlen sollen addiert werden?")
    while not (numOne := input("1. Zahl\n")).isnumeric():
        print("Es können nur zahlen übergeben werden")
    while not (numTwo := input("2. Zahl\n")).isnumeric():
        print("Es können nur zahlen übergeben werden")
    numOne = int(numOne)
    numTwo = int(numTwo)
    print(f"{numOne} + {numTwo} = {numOne + numTwo}")

# assignment expressions :=
# Erlaubt es uns variablen nur unter bestimmten Bedingungen einen Wert zuzuweisen
# Im obigen Beispiel wird numOne und numTwo erst zugewiesen, wenn ein rein numerischer String eingegeben wurde
# https://realpython.com/lessons/assignment-expressions/


# calc_loop()

# WIr können auch in andere Typen wie z.B. floats oder strings casten
# int(wert) => Versucht in einen integer mit Basis 10 zu konvertieren,
# falls z.B ein Buchstabe enthalten ist wird ein Fehler geworfen
# float(wert) => Versucht in eine Kommazahl mit Basis 10 zu konvertieren,
# falls z.B ein Buchstabe enthalten ist wird ein Fehler geworfen
# Floats müssen mit Punkten und nicht mit Kommas getrennt sein, ansonsten wird ein Fehler geworfen
# str(wert) => Wandelt eine Zahl oder ähnliches in einen String um


# def calc_loop():
#     print("Welche Zahlen sollen addiert werden?")
#     while not (numOne := input("1. Zahl\n")).isnumeric():
#         print("Es können nur zahlen übergeben werden")
#     while not (numTwo := input("2. Zahl\n")).isnumeric():
#         print("Es können nur zahlen übergeben werden")
#     numOne = int(numOne)
#     numTwo = int(numTwo)
#     print(f"{numOne} + {numTwo} = {numOne + numTwo}")

# Übung 2 Input:
# Erstelle eine Funktion, die Funktion soll den User einmal nach der gewünschten Rechenoperation fragen
# Der User kann entweder a oder s schreiben
# Bei a soll addiert werden
# Bei s soll subtrahiert werden
# Nach der Rechenoperation sollen zwei Zahlen abgefragt werden
# Nur Integer
# Am Ende soll die Konsole das Ergebnis ausgeben


def get_numbers():
    print("Welche Zahlen sollen addiert werden?")
    while not (numOne := input("1. Zahl\n")).isnumeric():
        print("Es können nur zahlen übergeben werden")
    while not (numTwo := input("2. Zahl\n")).isnumeric():
        print("Es können nur zahlen übergeben werden")
    numOne = int(numOne)
    numTwo = int(numTwo)
    return numOne, numTwo

def simple_calc():
    options = ["a", "s", "m"]
    print("Gültige Operationen:\n(a)ddieren | (s)ubtrahieren")
    choice = input("Welche Operation soll ausgeführt werden?\n").lower()
    while choice not in options:
        print("Ungültige Operation ausgewählt")
        choice = input("Welche Operation soll ausgeführt werden?\n").lower()
    numOne, numTwo = get_numbers()
    if choice == "a":
        print(f"{numOne} + {numTwo} = {numOne + numTwo}")
    else:
        print(f"{numOne} - {numTwo} = {numOne - numTwo}")


def simple_calc_alternative():
    options = ["a", "s", "m", "d"]
    print("Gültige Operationen:\n(a)ddieren | (s)ubtrahieren | (m)ultiplizieren | (d)ividieren")
    while not (choice := input("Welche Operation soll durchgeführt werden?\n").lower()) in options:
        print("Bitte wähle eine gültige Option.\n(a)ddieren | (s)ubtrahieren | (m)ultiplizieren | (d)ividieren")
    numOne, numTwo = get_numbers()
    if choice == "a":
        print(f"{numOne} + {numTwo} = {numOne + numTwo}")
    elif choice == "m":
        print(f"{numOne} x {numTwo} = {numOne * numTwo}")
    elif choice == "d":
        if numTwo == 0:
            print("Es kann nicht durch 0 geteilt werden.\nDie zweite Zahl wurde durch 1 ersetzt")
            numTwo = 1
        print(f"{numOne} / {numTwo} = {numOne / numTwo}")
    else:
        print(f"{numOne} - {numTwo} = {numOne - numTwo}")


# Erweitere die Funktion simple_calc oder simple_calc_alternative um die Möglichkeit der Multiplikation


simple_calc_alternative()
