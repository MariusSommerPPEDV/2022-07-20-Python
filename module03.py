import time

# Kontrollstrukturen

# if - Anweisungen

def is_even(number):
    # Syntax:
    # if Bedingung
    if (number % 2 == 0):
        print("Die Zahl ist gerade")
        return True
    # else
    else:
        print("Die Zahl ist ungerade")
        return False


def pythonic_is_even(number):
    return number % 2 == 0
    # Funktioniert identisch wie die Funktion is_even

# else muss immer nach einem if stehen
# if kann aber auch alleine stehen
# else braucht auch keine Bedingung

# Falls es mehr als zwei Fälle gibt:
# elif

def is_greater(number1, number2):
    if (number1 == number2):
        print("Beide Zahlen sind gleich groß")
    elif (number1 > number2):
        # elif benötigt eine Bedingung, da sie einen alternativen Fall prüft
        # elif kann nur nach einem if oder einem anderen elif stehen
        # das elif wird nur geprüft, falls das if nicht eintritt
        print("number1 ist größer")
    else:
        print("number2 ist größer")

# Bei der Kombination aus if, elif und else kann immer nur ein Fall eintreten
is_greater(12, 12)


def is_big(number):
    if (1000 < number):
        print("number ist größer als 1000")
    if (100 < number):
        print("number ist größer als 100")
    if (10 < number):
        print("number ist größer als 10")
    if (1 < number):
        print("number ist größer als 1")
    else:
        print("Die Zahl ist kleiner als 1")


def is_big_elif(number):
    if (1000 < number):
        print("number ist größer als 1000")
    elif (100 < number):
        print("number ist größer als 100")
    elif (10 < number):
        print("number ist größer als 10")
    elif (1 < number):
        print("number ist größer als 1")
    else:
        print("Die Zahl ist kleiner als 1")


is_big(5000) # Gibt alle print-Statements außer das des else Blockes aus
is_big_elif(5000) # Gibt nur das erste print-Statement zurück

# verkettete if Blöcke wie in der Funktion is_big machen dann Sinn wenn mehrere Fälle eintreten können
# Falls nur ein Fall eintreten kann, dann benutzt man if, elif und else

# Übung 2 - Funktionen:
# Wir wollen eine Funktion erstellen, die für uns zwei Zahlen dividiert
# Es soll sichergestellt werden, dass die zweite Zahl nicht 0 ist
# Falls die zweite Zahl null ist soll in der Konsole ausgegeben werden, dass man nicht durch 0 teilen kann
# Falls die zweite Zahl nicht null ist, soll die dividierte Zahl zurückgegeben werden
# Bsp: divide(8,0) => Konsole soll sagen es geht nicht
#      divide(8,4) => 2 soll zurückgegeben werden


# Kurzschreibeweise von if Bedingungen:

def single_line_if(number):
    if number % 2 == 0: print(number, "ist gerade")

# Falls if und else auf einer Zeile geschrieben werden sollen:

# Funktioniert identisch wie die Funktion auf Zeile 96
def single_line_if_else(numberOne, numberTwo):
    print(numberOne, "ist größer als", numberTwo) if numberTwo < numberOne else print(numberTwo, "ist größer als", numberOne)


def multiline_if_else(numberOne, numberTwo):
    if numberTwo < numberOne:
        print(numberOne, "ist größer als", numberTwo)
    else:
        print(numberTwo, "ist größer als", numberOne)


single_line_if(20)
single_line_if(23)

single_line_if_else(22, 12)
single_line_if_else(12, 33)

# Teränr Operator
# Ist sehr unleserlich und deutlich komplexer als eine normale if, elif Anweisung

def ternary(numberOne, numberTwo):
    print(numberOne, "ist größer als", numberTwo) if numberTwo < numberOne else (print("Die Zahlen sind gleich groß") if numberOne == numberTwo else print(numberOne, "ist kleiner als", numberTwo))


ternary(12, 24)
ternary(100, 12)
ternary(40, 40)

# Ifs können auch verschachtelt sein


def even_multiple_ten(number):
    if number % 2 == 0:
        print(number, "ist gerade.")
        if number % 10 == 0:
            print("Und die Zahl ist ein vielfaches von 10.")
        else:
            print("Und die Zahl ist kein vielfaches von 10.")
    else:
        print(number, "ist ungerade.")
        if number % 10 == 0:
            print("Und die Zahl ist ein vielfaches von 10.")
        else:
            print("Und die Zahl ist kein vielfaches von 10.")


# Die Schleifen:
# Alle Schleifen in Python sind Kopfgesteuert, d.h. die Bedingung wird am Anfang geprüft
# Gibt zwei Stück:
# 1. while
# 2. for

# while-Schleife:
# Syntax:
# Keyword: while Bedingung:
#       code-Block
# Wenn wir etwas bestimmt oft wiederholen wollen, brauchen wir eine Zähler Variable,
# die wir vor der Schleife definieren und innerhalb der Schleife hochzählen
# Schleifen können auch mit else kombiniert werden
# Das else wird nach beenden der Schleife ausgeführt

counter = 0  # Zähler-variable

while counter < 11:  # Start der Schleife und Endbedingung
    print(counter)
    counter += 1  # Hier wird der Zähler hochgezählt
#   counter = counter + 1 identisch zur Operation auf Zeile 155
else:
    print("while-Schleife ist vorbei.")

# Es kann nicht nur gezählt werden
# Jeder boolesche Ausdruck kann als Bedingung verwendet werden

# Übung 3 - Funktionen und Schleifen:

# Erstelle eine Funktion, die einen Zahl als Parameter erhält
# Innerhalb der Funktion soll eine while-Schleife sein, die bei 0 beginnt und bei der übergebenen Zahl endet
# Innerhalb der while-Schleife soll die is_even() Funktion aufgerufen werden
# Falls is_even() true zurückgibt, soll die Zahl in der Konsole ausgegeben werden
# andernfalls soll einfach weitergezählt werden
# range(start, ende, schrittweite)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def count(number):
    counter = 0
    while counter <= number:
        if is_even(counter):
            print(counter)
        counter += 1


def count_range(number):
    counter = 0
    while counter in range(0, number + 1, 1):
        if is_even(counter):
            print(counter)
        counter += 1


count(5)
print("count mit range:")
count_range(5)

# count(5)
# 0
# 2
# 4

# for-Schleife:

first_name = "Maximilian"

# syntax einfache for-Schleife:
# for (platzhalter für das derzeitige Element) in (Iterierbares Objekt):
for char in first_name:
    print(char)

# Funktioniert gut in Kombi mit ranges:

for number in range(0, 11):
    if is_even(number):
        print(number)

myList = ["Erstes Element", "Zweites Element", "Drittes Element"]

for list_item in myList:
    print(list_item)

print(len(myList))
for counter in range(len(myList)):
    print(myList[counter], "ist ein Element der Liste")
else:
    print("For ist vorbei")

# Formatted-Strings in Python:

# Syntax: f"{variable}", dadurch wird die Variable direkt eingesetzt
print(f"My name is {first_name} and I'm 29 years old.")
print("My name is", first_name, "and I'm 29 years old.")


for i in range(0,11):
    if is_even(i):
        print(f"{i} ist gerade")

# Syntax for:
# for (platzhalter) in (Iterierbares Objekt):
#   print(platzhalter)
# if platzhalter....

# Übung 4 - Funktionen:
# Erstelle eine Funktion, die von 0 bis 100 hochzählt und jede Zahl auf ihre Teilbarkeit durch 3 und 5 prüft
# Wenn die Zahl weder durch 3 noch durch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# Wenn die Zahl nur durch 3 teilbar ist soll "Fizz" ausgegeben werden
# Wenn die Zahl nur durch 5 teilbar ist soll "Buzz" ausgegeben werden
# Wenn die Zahl durch 5 und 3 teilbar ist soll "FIzzBuzz" ausgegeben werden
# if x % 3 == 0 and x % 5 == 0


def fizzBuzz():
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


def fizzBuzz_alt():
    for num in range(101):
        answ = ""
        # DUrch einfach ifs wird jedesmal geprüft und, falls die Zahl teilbar ist
        # wird Fizz bzw Buzz an den Antwortstring gehängt
        if num % 3 == 0:
            answ += "Fizz"
        if num % 5 == 0:
            answ += "Buzz"
        # Hier wird geprüft ob der String leer ist, wenn ja war die Zahl durch nichts teilbar und sie wird einfach
        # in der Konsole ausgegeben
        if answ == "":
            print(num)
        # Falls die Antwort nicht leer ist wird sie hier ausgegeben
        else:
            print(answ)


fizzBuzz_alt()

#FizzBuzz
#1
#2
# Fizz
# 4
# Buzz
# Fizz
# ...
# 14
# FizzBuzz


# Schleifen können auch verschachtelt werden
myList2 = [
    ["Max", "Mustermann"],
    ["Erika", "Musterfrau"],
    ["Sven", "Olfason"]
]

print(myList2)  # Hier wird die ganze mehrdimensionale Liste ausgegeben
print(myList2[0])  # Hier wird nur die erste enthaltene Liste ausgeben
print(myList2[0][1])  # Hier greife ich auf das zweite Element der ersten Liste zu

for liste in myList2:
    print(liste)
    for name in liste:
        print(name)
        # Erst wenn die innere Schleife ganz durchschritten ist, wird die äußere fortgeführt


# EIne Uhr ist nichts anderes als eine dreifach verschachtelte Schleife

for hours in range(2): # Kann erst um eine Position vorrücken wenn die Minuten Schleife feritg ist
    for minutes in range(60):  # Kann erst durchlaufen wenn die Sekunden Schleife fertig ist
        for seconds in range(60):
            print(f"{hours}:{minutes}:{seconds}")

# Übung 5 - Funktionen:

# Schreibe eine Funktion, die uns das gesamte kleine einmaleins vorrechnet
# Jeder Schritt soll in folgendem Format in der Konsole ausgegeben werden:
# 1er Einmaleins:
# 1 x 1 = 1
# ...
# 1 x 10 = 10
# 2er Einmaleins
# 2 x 1 = 2
# ....
# 2 x 10 = 20

def einmaleins():
    for factor in range(1, 11):
        print(f"Das {factor}er Einamleins")
        for multiplier in range(1, 11):
            print(f"{factor} x {multiplier} = {factor * multiplier}")

einmaleins()


# Das = nach dem Parameter Namen definiert einen default-Wert, dieser wird immer dann verwendet
# wenn kein Wert übergeben wurde
def einmaleins_with_limit(limit=10):
    for factor in range(1, limit + 1):
        print(f"Das {factor}er Einamleins")
        for multiplier in range(1, 11):
            print(f"{factor} x {multiplier} = {factor * multiplier}")


# einmaleins_with_limit() # funktioniert nicht, da wir keinen Parameter übergeben
# Kann mittels default Argumenten vorgebeugt werden
einmaleins_with_limit()  # Ohne Parameter wird nun die 10 als Limit benutzt

einmaleins_with_limit(20)

# def divide(numOne=None, numTwo=None):
# Hier teilen wir dem Benutzer mit, dass Parameter übergeben werden ohne dass unser Programm abbricht
#     if numOne is None or numTwo is None:
#         print("Es müssen zwei Parameter übergeben werden")
#     else:
#         return numOne / numTwo


def divide(numOne=1, numTwo=1):
    return numOne / numTwo


divide()  # Hier wird 1 / 1 gerechnet
divide(12)  # Hier wird 12 / 1 gerechnet
divide(55, 6)  # Hier wird 55 / 6 gerechnet
# Standardmäßig ist jeder Parameter, den wir in eine Funktion einbauen ein so genanntes Keyword-Argument
divide(numTwo=50)  # Jetzt wird 1 durch 50 geteilt, da ich explizit numTwo befüllt habe
divide(numTwo=12, numOne=75)

# Arbitrary Arguments
# Um einen Parameter als Arbitrary Argument auszuzeichnen wird das * Symbol benutzt


def add_numbers(*numbers):
    # Die Funktion wird jetzt beliebig viele Zahlen akzeptieren und sie in ein Tupel packen => Wir sollten iterieren
    result = 0
    for num in numbers:  # Der Stern wird nur beim Parameter, aber nicht mehr innerhalb der Funktion benötigt
        result += num
    return result


print(add_numbers(1, 4, 8, 9, 12, 66, 5, 3, 333, 19))
print(add_numbers(1, 4, 8, 9))
print(add_numbers(1))
print(add_numbers(1, 4, 8, 9, 12, 66, 5, 3, 333, 19,123,12431,532523,32523523,51241243))

# Arbitrary Arguments geben uns die Möglichkeit mit einer unbekannten Anzahl von Parametern zu arbeiten
# Können dafür aber nicht mehr als Keyword benutzt werden
# add_numbers(numbers=123) => unexpected Keyword Argument

# Arbitrary Keyword Arguments
# Werden mit zwei * Symbolen gekennzeichnet


def random_stuff(**keywords):
    print(keywords)
    for key in keywords:
        # keywords wir nun wie ein Dictionary behandelt
        print(keywords[key])
        print(key)


random_stuff(key1=12, zeug=15, test="Hallo")
# {key:12, zeug:15, test:"Hallo"}

# Es können auch beide kombiniert werden
# Dann muss auf die Reihenfolge geachtet werden


def combined_args(*args, **kwargs):
    print(args)
    print(kwargs)


combined_args(12, 5123, "Hallo", "test", test=123124, vier=4, iwas="Bye", kwargs=123)
# Alle Parameter ohne keyword werden zum Tupel gepackt, alle mit Keyword werden in ein dicitonary gepackt

# Standardmäßig sind alle Parameter Keyword-Arguments
# Kann aber auch verhindert werden
# Wir können erzwingen, dass es positional arguments sind
# d.h. sie werden in der Reihenfolge befüllt, wie sie in der Klammer haben


def divide_no_keyword(numOne=5, numTwo=1, /):
    # Wenn ein slash nach Paramtern angegeben wird, gelten diese als positional only
    return numOne / numTwo


divide_no_keyword(2, 14)
# divide_no_keyword(numTwo=12)  Funktioniert nicht, da die Paramtern nicht mehr per Keyword befüllt werden können


# Rekursive Funktionen
# Ist grundsätzlich eine Funktion, die sich in ihrem Körper nochmal aufruft
# In Python ist die rekursion auf 1000 Schritte begrenzt


def factorial(number):
    # Eine Rekursive Funktion braucht immer einen Ausstiegspunkt => Wir benutzen dafür if
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))
# print(factorial(1001)) Python bricht die Ausführung nach 1000 Aufrufen ab, da es zu ineffizient ist


def factorial_loop(number):
    sum = 1
    for i in range(number, 0, -1):
        sum *= i
    return sum

# Hier timen wir die rekursive Funktion
start_time = time.time()
result = factorial(998)
end_time = time.time()

print(result)
print(f"Es sind {end_time - start_time} Sekunden vergangen")

# Hier timen wir die Funktion mit der Schleife
start_time = time.time()
result = factorial_loop(1500)
end_time = time.time()

print(result)
print(f"Es sind {end_time - start_time} Sekunden vergangen")


# Unpacking Operatoren

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Wenn ich einen * vor ein iterierbares Objekt setzte wird dieses in seine einzelnen Elemente aufgespalten
# Der * wird für Objekte mit Index verwendet
print(add_numbers(*number_list))

# Unpacking Operator bei Dicitonaries
myDict = {"firstName": "Max", "lastName": "Mustermann", "age": 25}
# ** werden hier benutzt
random_stuff(**myDict)
random_stuff(firstName="Max", lastName="Mustermann", age=25)


def check_age(**kwargs):
    if kwargs["age"] >= 18:
        print("Erlaubt")
    else:
        print("Zu jung")


check_age(**myDict)

myDict2 = {"firstName": "Max", "lastName": "Mustermann", "age": 12}

check_age(**myDict2)

# Übung 5 - Funktionen:
# Erstelle eine Funktion, die einen String als Paramter erhält
# Die Funktion soll über den String iterieren und soll am Ende in der Konsole ausgeben, aus wie vielen
# klein bzw großbuchstaben der String besteht

def count_case_old(word):
    count_lower = 0
    count_upper = 0
    count_special = 0
    for character in word:
        if character.lower() == character.upper():
            count_special += 1
        elif character == character.lower():
            count_lower += 1
        else:
            count_upper += 1
    print(f"klein: {count_lower}  groß: {count_upper} | sonder: {count_special}")


def count_case(str):
    """
    Eine Funktion, die in der Konsole ausgibt wie viele Klein- und Großbuchstaben,
    sowie Sonderzeichen in einem String entahlten sind
    :param str: Der Satz, der geprüft werden soll
    :return: None
    """
    lower = 0
    upper = 0
    not_alpha = 0
    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            not_alpha += 1
    print(f"klein:{lower}, groß:{upper}, andere:{not_alpha}")


# count_case("TeSt")
# klein: 2 groß: 2

count_case_old("123Test...   asdasd ")
count_case("123Test...   asdasd ")
"test".upper()
"tesT".islower()


