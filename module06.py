# Lambdas und die höheren Funktionen

# Lambdas
# Lambdas sind grunsätzlich anonyme Funktionen, also eine Funktion, die keinen Namen erhält
# Sie werden mit dem Lambda Keyword definiert
# In Python sind FUnktionen Objekte erster Klasse, d.h. sie können Variablen zugewiesen werden

def add_number(numberOne, numberTwo):
    return numberOne + numberTwo

add_number(10, 5)

add = add_number # Hier ohne Klammern, da ich die FUnktion nicht ausführe,
# sondern einer Variable eine Referenz auf die Funktion zuweise

print(add(12, 60))
# add ist jetzt einfach ein Alias für die Funktion add_number()

# Bei normalen Funktionen noch nicht so nützlich, aber Lambdas, die normalerweise keinen Namen haben, sehr nützlich
# Dadurch können sie mehrfach ausgeführt werden

lambda_add = lambda numberOne, numberTwo : numberOne + numberTwo
# Das return wird hier impliziert, also muss ich es nicht selbst schreiben

print(lambda_add(50, 25))

# Normalerweise werden Lambdas nicht einer Variable zugewiesen, sondern einer anderen Funktion als Parameter übergeben

# Lambda als Parameter:
# Meist bei höheren Funktionen
# Eine höhere Funktion ist eine Funktion, die als Parameter eine andere Funktion erwartet
# Beispiel: filter()
# Syntax der filter-Funktion:
# filter(funktion, iterierbaresObjekt)
# z.B. können wir eine Zahlenliste filtern, um nur noch gerade Zahlen zurückzuerhalten
# filter gibt ein Filter-Objekt zurück => list-constructor oder ähnliche muss darauf angewendet werden

number_list = list(range(0, 101))
print(number_list)
even_numbers = filter(lambda current_number: current_number % 2 == 0,
                      number_list)
# filter wendet nun die Lambda-Funktion auf jedes Element der number_list an
# Wenn die Lambda Funktion True zurückgibt, wird das derzeitige Element zum filter-Objekt hinzugefügt
# Wenn die Lambda Funktion False ergibt, wird das derzeitige Element nicht hinzugefügt


def is_even(number):
    return number % 2 == 0


even_numbers_def = filter(is_even, number_list)


# So wird nur ausgegebn, dass es ein Filter Objekt ist und wo es im Speicher liegt
# => Muss erst noch in Liste umgewandelt werden
print(even_numbers)
print(even_numbers_def)

even_numbers = list(even_numbers)
even_numbers_def = list(even_numbers_def)

print(even_numbers)
print(even_numbers_def)

# Wenn ich eine Funktion mit def erstelle, wird sie über das gesamte Skript im Speicher gehalten, da sie jederzeit
# eingesetzt werden könnte
# Das lambda hingegen verbraucht nur so lange Speicher, bis es fertig ausgeführt wurde, danach wird es "weggeworfen"
# Das lambda Keyword wird nur benutzt, wenn ich eine neue Lambda Funktion definiere


# Übung 1 - Lambdas:
# Erstelle eine Zahlen-Liste, die bei 10 anfängt und bei 200 endet
# Filter die Liste nun auf Vielfache von 15
# Benutze dafür eine Lambda-Funktion
# Wandel anschließend das Filter-Objekt in eine Liste um

list10to200 = list(range(10, 201))
multi15list = filter(lambda current_number: current_number % 15 == 0,
                     list10to200)
multi15list = list(multi15list)
print(multi15list)


# map Funktion
# map(FunktionDieAufJedesElementWirkt, IterierbareObjekt)
# Gibt ein map-Objekt zurück => muss also auch gecasted werden

string_list = [
    "Max",
    "Erika",
    "Sven"
]
# [ ["M", "a", "x"], ["E",.....]

print(list("Test"))

char_list = map(list, string_list)
# list("Max"), list("Erika")

print(char_list)
char_list = list(char_list)
print(char_list)

# map erwartet keinen booleschen Wert

upper_names = list(map(lambda name: name.upper(), string_list))
print(upper_names)


def make_upper(name):
    return name.upper()


upper_names2 = map(make_upper, string_list)
upper_names2 = list(upper_names2)
print(upper_names2)

# Übung 2 - map:
list10to200 = list(range(10, 201))
multi15list = filter(lambda current_number: current_number % 15 == 0,
                     list10to200)
multi15list = list(multi15list)
print(multi15list)


# Wir wollen nun die multi15list verändern
# Wir wollen die map Funktion benutzen, um jedes Element der multi15list zu verdreifachen
# Anschließend soll wieder eine liste daraus erstellt werden
# Lambda verwenden

multi15list = map(lambda current_number: current_number * 3, multi15list)
multi15list = list(multi15list)
print(multi15list)

# Höhere Funktionen:
# Funktion, die eine weitere Funktion, als Paramter erwartet
# Die übergebene Funktion wird oft callback genannt, da sie erst später aufgerufen wird, sie wird sozusagen zurückgerufen


def my_higher_function(functionReference, data):
    return functionReference(data)


print(my_higher_function(lambda x: x*5, 10))

# my_higher_function(lambda x: x*5, 10)
#   return lambda 10: 10 * 5

my_higher_function(is_even, 15)
#  my_higher_function(is_even, 15)
#   return is_even(15)


def my_filter(functionRef, liste):
    return_list = []
    for element in liste:
        if functionRef(element):
            return_list.append(element)
    return return_list


my_even_nums = my_filter(is_even, number_list)
print(my_even_nums)

my_multi8 = my_filter(lambda x: x % 8 == 0, number_list)
print(my_multi8)

# Type-Annotation
# Gibt uns die Möglichkeit anderen programmieren Hinweise zu geben, wie unsere Funktionen aufzurufen sind


def multiply_numbers(numberOne: float, numberTwo: int) -> float:
    """
    Multipliziert numberOne mit numberTwo
    :param numberOne:
    :param numberTwo:
    :return:
    """
    return numberOne * numberTwo


result = multiply_numbers(12.45, 55)

print(result)
# Die Annotation ist wirklich nur ein Hinweis und erzwingt nichts
# Ist aber trotzdem sehr hilfreich, daich dann aus der Funktionssignatur lesen kann, was erwartet wird
# Am besten Type-Annotation und Docstring
# Wenn möglich bei jeder Funktion einbauen
