# Filehandling in Python

# Zum bearbeiten von Textdateien existiert die Funktion open()
# open() akzeptiert zwei Parameter
# 1. Dateiname+ Endung
# 2. Modues, in dem die Datei geöffnet werden soll
# Folgende Modi existieren:
# "r" - read, kann nur Dateien lesen und nichts schreiben. Falls die Datei nicht existiert, wird ein Fehler geworfen
# "a" - append, kann Inhalt nicht lesen, aber neuen Inhalt am Ende der Datei anfügen
#  Erstellt die Datei, falls sie noch nicht existiert
# "w" - write, erlaubt Inhalt in die Datei zu schreiben, aber nicht zu lesen
# Falls die Datei nicht existiert wird sie erstellt
# Falls sie existiert und Inhalt hat, wird dieser überschrieben
# "x" - create, Erstellt die Datei, falls sie bereits existiert wird ein Fehler geworfen, kann schreiben

# Erstellen einer Datei und schreiben von Inhalt
# Muss einer Variable zugewiesen werden, da die Datei im Speicher gehalten wird

# file = open("demo1.txt", "x")
# Wenn ich keinen Pfad mitangebe, wird die Datei im derzeitigen Ordner erstellt/gesucht
try:
    file = open("./test/demo2.txt", "x")  # ERstellt die Datei, falls sie nicht existiert
    file.write("Test")
except FileExistsError as e:
    print("Datei wird nicht erstellt, da sie bereits existiert")
    file = open("./test/demo2.txt", "a")
    print("Was soll angehängt werden?")
    file.write("\n")
    new_line = input("")
    new_line += "\n"
    file.write(new_line)  # Die methode write() Fügt ihren Parameter an die Datei an
    file.write(new_line)  # Fügen die selbe Zeile nochmal an um mehr Text zu haben
    # Alternativ zu write() gibt es writelines()
    # writelines() akzeptiert ein iterierbares Objekt als Parameter und fügt jedes Element an die Datei an
    lines = ["\nzeile1", "\nzeile2", "\nzeile3"]
    file.writelines(lines)
    # weder writelines() noch write() erzwingt eine neue Zeile, die müssten wir selbstständig mit dem \n hinzufügen
    # Um auf Nummer sicher zu gehen, sollten wir Dateien nach dem Öffnen auch schließen
    # Dafür rufen wir die methode close() auf
    file.close()


# Damit wir nicht vergessen die Datei zu schließen können wir auch das with-statement benutzen
# Datei einlesen und in Python ausgeben
# Wird auch Context-Manager genannt

# try:
#     with open("./test/demo2.txt", "r") as demo_file:
#         print(demo_file.readline())  # Liest eine einzige Zeile aus
#         print(demo_file.readline())  # Liest eine einzige Zeile aus
#         # readline() gibt alles bis zum nächsten zeilenumbruch aus
#         print("readline endet")
#         print(demo_file.read())
#         # Read gibt die gesamte Datei aus, außer dem Teil, der bereits eingelesen wurde
# except FileNotFoundError:
#     print("Datei existiert nicht")

# Dateien können auch in read und write Modus gleichzeitig geöffnet sein

# with open("./test/demo2.txt", "w+") as file:  # w+ öffnet die Datei zum lesen und schreiben
#     print("Write and Read mit w+")
#     file.write("Test")
#     file.write("Test")
#     file.write("Test")
#     file.write("Test")
#     print(file.readline())
# w+ überschreibt die bestehende Datei


# r+ Funktioniert nur wenn die Datei bereits existiert, überschreibt sie dafür aber nicht
with open("./test/demo2.txt", "r+") as file:  # r+ öffnet die Datei zum lesen und schreiben
    print("Write and Read mit r+")
    print(file.read())
    file.write("Test")







