# Exception Handling in Python

def get_number():
    number = input("Gib mir eine Zahl.")
    return try_parse_float(number)

def try_parse_float(number_string):
    # Python kann versuchen etwas auszuführen
    try:  # Ist wieder ein Block, also eingerückt weiterschreiben
        return float(number_string)
    except:  # except erwartet einen Fehler im try-Block, falls ein Fehler auftritt wird alles im except Block ausgeführt
        print("Der übergebene String kann nicht in einen Float umgewandelt werden")
        # Try und except beenden das Programm nicht im Fehlerfall


def isfloat(number_string):
    try:
        float(number_string)
        return True
    # Wenn der number_string in einen float umgewandelt werden kann, wird nun True zurückgegeben
    except ValueError as error_message:
        print(error_message)
        return False
    except NameError as e:
        print(e)


def get_float():
    while not isfloat(numOne := input("1. Zahl\n")):
        print("Es können nur zahlen übergeben werden")
    while not isfloat(numTwo := input("2. Zahl\n")):
        print("Es können nur zahlen übergeben werden")
    numOne = float(numOne)
    numTwo = float(numTwo)
    return numOne, numTwo


zahl = get_float()
print(zahl)

# try kann nicht alleine stehen, mindestens ein except oder finally Block danach ist Pflicht

# try: Wird immer als erstes ausgeführt, falls er ohne Fehler durchläuft wird except übersprungen
# except: Wird ausgeführt, falls try Fehlschlägt und der richitge Error-Type geworfen wurde
# else: Wird nur ausgeführt, wenn der except Block nicht ausgeführt wurde
# finally: wird immer ausgeführt, egal ob es eroflgreich war oder nicht


def try_except_else_finally(testValue):
    try:
        print("Try-Block")
        print(testValue)
    except NameError as e:
        print("Except-Block:")
        print(e)
    else:
        print("Hallo aus dem else-Block")
        print("Try wurde erfolgreich ausgeführt")
    finally:
        print("Hallo aus finally")
        print("Ich werde ausgeführt egal, ob ein Fehler geworfen wurde oder nicht")


try_except_else_finally("Hallo")

# Ich kann Fehler auch erzwingen
# Dafür kann das raise-Keyword benutzt werden


def max_10(number):
    try:
        if number > 10:
            raise ValueError(f"Maximaler Wert beträgt 10. Übergebener Wert ist {number}")
        else:
            print("GUt gemacht!")
    except ValueError as e:
        print(e)
        print("Es darf maximal 10 übergeben werden")

max_10(10)
max_10(15)

# Mit raise kann ich jederzeit Fehler erheben
# Wenn ich danach eine eigenen Message schreiben will benötige ich runde Klammern nach dem ErrorType

# Übung 1 - Try Except:
# Schreibe eine Funktion, die zwei Zahlen dividiert
# Wenn 0 übergeben wird, soll das Programm nicht crashen, sondern eine Nachricht in der Konsole anzeigen, dass
# Divisionen durch 0 nicht möglich sind


def divide(numberOne, numberTwo):
    try:
        if numberTwo == 0:
            raise ZeroDivisionError("Test")
        return numberOne / numberTwo
    except ZeroDivisionError as e:
        print(e)
        print("Durch 0 kann man nicht teilen.")
    except TypeError as e:
        print("Es können nur Zahlen und keine Strings übergeben werden")


result = divide(25, 45)
print(result)
divide(415, 0)
