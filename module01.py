print("Hallo Welt!")
# Ich bin ein Kommentar
# Strg + Umschalt + F10 führt die derzeit ausgewählte Datei aus
print("Ich bin eine weitere Zeile")
# Print gibt Text oder Variablen in der Konsole aus

# Syntax:

# Keine Semikolons
# Keine geschweiften Klammern bei den Blöcken
# Einschübe sind wichtig, sie ersetzen in Python die geschweiften Klammern und symbolisieren Blöcke
# Case-sensitive

# Variable definieren:
# Setzt sich zusammen aus:
# Identifier = Wert
# Identifier ist eine Referenz auf einen Punkt im Speicher und enthält einen Wert

name = "Marius Sommer"
xyz = "Test"
zahl = 123
zahlZwei = 1.25

# Variablen können verändert werden, auch ihr Typ
name = 55

# Zahlen können potenziell unbegrenzt groß sein


# Datentypen in Python:

# String
# Text-Typ
# Wird von Anführungszeichen umgeben
# Es geht sowohl " als auch '
stringVar = "1234 muss 78=)() \" \nTest12314151254"
# Wenn wir die selben Anführungszeichen innerhalb des Textes benutzen will, wie auch zur Definition des Strings benutzt
# wurden müssen sie mittels \ escaped werden
# \n => Wird ein Zeilenumbruch
print(stringVar)
# Strings verfügen über Indizes
# Indizes beginnen bei 0
#  Wir können ienzelnen Zeichen innerhalb des Strings mit ihrem Index ansprechen
# Dafür benutzen wir die Klammernschreibweise
print(stringVar[5])
# string[index] => Gibt uns das Zeichen an der Position index zurück
singleChar = stringVar[5]
print(singleChar)
# Python erlaubt es uns substrings mit der Klammernschreibweise zu erzeugen
# Wird slicing genannt
# string[0:5] => gibt uns die ersten 5 Zeichen des Strings zurück, Indexposition 5 ist dabei nicht inkludiert
# Syntax: stringIdentifier[startposition:endposition:schrittweite]
# DIe Endposition ist dabei nicht inkludiert
print(stringVar[0:5]) # Gibt uns die Zeichen von Index 0 bis Index 4 zurück
print(stringVar[0:8:3]) # Gibt uns die Zeichen von Index 0 bis Index 7 in 3er Schritten zurück
print(stringVar[20:]) # Gibt uns alle Zeichen beginnen bei Index 20 zurück

# Der Datentyp String verfügt über mehrere Methoden
# Sie werden wie folgt aufgerufen:

print(stringVar.count("1"))
# Die count Methode zählt wie oft der Ausdruck innerhalb der Klammern im String vorkommt

# var.isalpha()
# isalpha prüft ob der aufrufende String nur aus Buchstaben besteht
print(stringVar.isalpha()) # => False

# var.isnumeric()
# Prüft ob der aufrufenden String nur aus Zahlen besteht
print(stringVar.isnumeric()) # => False

# var.isalnum()
# Prüft ob der String nur aus Buchstaben und Zahlen besteht
print(stringVar.isalnum()) # => False

# var.lower() wandelt den String in Kleinbuchstaben um
# var.upper() wandelt den String in Großbuchstaben um
# Beide Methoden geben dabei einen neuen String zurück und verändern den bestehenden nicht
upperString = stringVar.upper()
print(upperString)

lowerString = stringVar.lower()
print(lowerString)

# var.title() => Jeder Anfangsbuchstabe eines Wortes wird großgeschrieben
# var.capitalize() => Nur der Anfangsbuchstabe des Strings wird groß
print(stringVar.capitalize())  # ändert den String nicht, da er nicht mit einem kleinbuchstaben beginnt
print(stringVar.title())

# var.replace(UrsprünglichesZeichen, neueZeichen)
bspString = "HhhhhHHHHHhhhhh"
print(bspString.replace("H", "098"))

# String-Methoden: https://docs.python.org/3/library/stdtypes.html?highlight=str#str

# Numerischen Datentypen:

# int - Ganzzahlen
# float - Kommazahlen
# complex  - Komplexe Zahlen

intVar = 15
floatVar = 15.5
complexVar = 1j * 5j

# type(var)
# Gibt den Typen der Variable zurück
print(type(intVar))
print(type(floatVar))
print(type(complexVar))

# Mathematische Operationen:
# + Addieren
# - Subtrahieren
# / Division
# * Multiplizieren
# % Modulus / Teilung mit Rest
# ** Potenz, alternativ dazu pow(x, y) => x ** y
# // floor division, teilt und rundet auf die nächste Ganzzahl ab

# bool
# Mögliche Werte:
# True
# False

# Logische Operatoren in Python
# is - Prüft ob die beiden Objekte identisch sind
# is not - Prüft ob es nicht die selben Objekte sind
# in - Prüft ob der Wert links vom in in dem Objekt rechts vom in enthalten ist
# not in - Prüft ob der Wert links vom in nicht in dem Objekt rechts vom in enthalten ist

# and - Erfordert, dass alle verknüpften Bedingungen wahr sind
# or - Erfordert, dass mindestens eine der verknüpften Bedingungen wahr sind

# Lists
# Sind geordnet
# Verfügen über Index
# Duplikate sind erlaubt
# Sind veränderbar
# Können verschiedenen Typen enthalten

myList1 = [1, 2, 3, True, "Test"]
myList2 = list(bspString)  # Erlaubt das Umwandeln von iterierbaren Objekten in Listen

print(myList2)
print(myList1)
print(type(myList1))

# Einzelne Elemente in der Liste ansprechen:
# list[index] => Gibt uns das Element an der Position index zurück
# Index beginnt hier auch mit 0

print(myList1[3])

# Methoden der Liste:

# Gesamte Liste leeren:
myList2.clear()
print(myList2) # Löscht alle Elemente aus myList2

# list.count("element") Zählt wie oft "element" in der Liste enthalten ist

print(myList1.count(3))

# Liste kopieren:
myList2 = myList1.copy()
print(myList2)
print(myList2 is myList1)  # False, da die Listen zwar dieselben Werte enthalten, aber an
# verschiedenen Punkten im Speicher liegen
print(myList2 == myList1)  # True, da hier nur die Werte verglichen werden

# Liste mit iterierbaren Objekten erweitern


myList1.extend(myList2)  # Hier wird eine ganze Liste angefügt
myList1.extend("test")  # Trennt den String in die einzelnen Buchstaben auf und fügt jeden als neues Element hinzu
print(myList1)

myList1.extend(myList1)  # Geht auch mit sich selbst
print(myList1)

# Liste um einzelnens Element erweitern

myList1.insert(0, "6")  # Fügt an der angegebenen Stelle das neue Element an,
# bestehende Elemente werden dabei verschoben, aber nicht ersetzt
print(myList1)
myList1.insert(0, myList2[4])  # Das 5. Element der Liste 2 wird am Anfang der myList1 angefügt

# list.append(element)
myList2.append(5)  # 5 wird an das Ende der Liste angefügt
print("Element anfügen")
print(myList2)

# Liste umdrehen
myList1.reverse()
print(myList1)

# Elemente aus einer Liste entfernen

# Element an einer bestimmten Position entfernen
myList1.pop(3)
print(myList1)

# Element mit bestimmten Wert entfernen
myList1.remove(True)
print(myList1)
# Wenn Duplikate vorhanden sind, wird immer nur das erste Auftreten des Wertes entfernt

# Liste sortieren
myList2 = [10000, 4424, 55, 1,2,3,4,5,99,566, -50]
myList2.sort()
# Standardmäßig wird alphanumerisch aufsteigend sortiert


print(myList2)

# Tuple, Set, Dictionaries

# Tuple
# sind geordnet
# verfügen über Index
# können duplikate enthalten
# können verschiedene Datentypen enthalten
# Elemente in einem Tupel sind nicht änderbar
# Tuple werden mit runder Klammer definiert
# Gibt auch den Konstruktor tuple(iterierbaresObjekt)

myTuple = (1, 2, 3, 4)
print("Tuple:", myTuple)
# myTuple[2] = 12 Funktioniert nicht, da Tuple-Elemente nicht neu zugeordnet werden können
print("Liste: ", myList2)
myList2[0] = 123
print(myList2)

# Trick um ein Tupel zu verändern:

myTuple = list(myTuple)  # Hier wird ein Tupel in eine Liste umgewandelt
myTuple[0] = 123  # Listen sind veränderbar, also klappt hier die neuzuweisung
myTuple = tuple(myTuple)  # Hier wird die Liste wieder in ein Tupel umgewandelt
print(myTuple)

# Methoden der Tupel

# tuple.count(element) - Gibt zurück wie oft element im tuple enthalten ist
print(myTuple.count(4))

# tuple.index(element) - Gibt zurück an welcher Indexposition element steht

print(myTuple.index(2))
print(myTuple[1])


# range()
# Nicht veränderbare Sequenz von Zahlen
# Syntax:
# range(10) => Gibt uns eine Range zurück, die die Zahlen von 0 bis 9 enthält
# range(startzahl, endzahl) => Gibt eine range beginnend bei Startzahl und endend bei Endzahl - 1 zurück
# range(startzahl, endzahl, schrittweite)

myRange1 = range(20)
print("range ohne Startzahl als Liste", list(myRange1))
myRange2 = range(50, 60)
print("range mit start- und endzahl als Liste", list(myRange2))
myRange3 = range(0, 110, 10)
print("range mit start- und endzahl sowie schrittweite als Liste", list(myRange3))

# Dictionaries
# Sammlung von Schlüssel und Wert Paaren
# sind geordnet
# sind veränderbar
# Duplikate sind nicht erlaubt

myDict = {
    "hierGehtAlles": "Value",
    "Key2": 12,
    "Key3": True,
    "Key4": [1, 2, 3, 4],
    "1": 123,
    2: 55,
    "2": 250
}

# Wenn ich den Wert eines Schlüssels erhalten will, nutze ich die Klammernschreibweise
# und übergebe den Namen des Schlüssels
print(myDict["2"])
print(myDict[2])
myDict["2"] = "Neuer Wert"
print(myDict["2"])

# Methoden:

# Ändern eines Wertes
# dict.update({"key": "neuer Wert"})
# Muss ein Dictionary als Parameter erhalten
myDict.update({"2": 255})
print(myDict)

# dict.clear()
# Löscht den Inhalt des Dictionaries

# dict.copy()
# Gibt eine Kopie des Dictionaries zurück

# dict.keys()
# Gibt uns eine Liste aller Schlüssel des Dictionaries zurück

print(myDict.keys())

# dict.items()
# Gibt uns eine Liste von Tupel zurück, jedes TUpel besteht aus einem Schlüssel und dessen Wert

print(myDict.items())

# dict.pop(schlüssel)
# Löscht den angegebenen Schlüssel und dessen Wert
myDict.pop("2")
print(myDict)

# dict.popitem()
# Löscht das letzte key-value Paar
myDict.popitem()
myDict.popitem()
print(myDict)

# dict.values()
# GIbt uns eine Liste aller Werte zurück
print(myDict.values())

# Hinzufügen von neuen Schlüsseln
# 1. Möglichkeit:

myDict["neuerSchlüssel"] = 12
print(myDict)

# 2. Möglichkeit:
# dict.setdefault(schlüssel, wert)
# Falls der Schlüssel bereits existiert wird sein Wert zurückgegeben
# Falls nicht wird der Schlüssel mit dem Wert erstellt
print(myDict.setdefault("neuerSchlüssel2", 14))
print(myDict)

# Sets
# sind nicht geordnet
# haben keinen index
# können über keine duplikate verfügen
# Es können neue Elemente hinzugefügt werden, aber bestehende können nicht verändert, aber entfernt werden

mySet = {1, 2, 2, 2, 3, 4, 5, 6}
print(mySet)  # Die 2 wird nur einmal aufgelistet, da das Set keine duplikate anzeigen kann

# Häufige methoden:

# set.clear() => leert das set
# set.copy() => gibt Kopie von dem Set zurück
# set.pop() => Entfernt das erste Element aus dem Set und gibt es zurück
# set.remove(element) => Entfernt das angegebene Element aus dem Set, falls das ELement
# nicht existiert wird ein Fehler geworfen
# set.update(element) => Fügt ein neues Element an das Set an

print(mySet.pop())
print(mySet.pop())
print(mySet)

# print(mySet.remove(20))
mySet.update([50])
print(mySet)

# Übung Modul1:

# Erstellt eine Collection, die alle Teilnehmer enthält
# Lasst einmal die gesamte Collection in der Konsole ausgeben
# Fügt anschließend ein neues Element an die Collection an und lass nur das neue Element in der Konsole ausgeben
