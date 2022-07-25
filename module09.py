# Datenbankverbindung
# Mit sqlite
# Dafür benötigen wir das Modul sqlite3

import sqlite3 as sql

# Wie erstelle ich eine Datenbank:

# Verbindet sich mit der Datenbank, falls sie nicht existiert wird sie erstellt
conn = sql.connect("testDatabase.db")
c = conn.cursor()

c.execute("create table if not exists User (userId, userName)")

c.execute("Insert into User values (1, 'klaus')")

userId = 2
userName = "tobias"

c.execute("insert into User values (?, ?)", (userId, userName))  # Wenn ich (?,?) verwende müssen Tuple übergeben werden
# Das Tupel muss genau so viele Werte enthalten wie wir Values befüllen wollen

c.execute("select * from USER ")
print(c)  # Git nur aus, dass es sich um ein Objekt der Cursor Klasse handelt
# => Brauchen dafür Fetch

# fetchone() => Gibt eine Zeile wieder, Rückgabetyp ist Tupel
# fetchmany(integer) => Gibt so viele Zeilen zurück wie wir angegeben haben, gibt diese als Liste zurück
# fetchall() => Gibt alle Zeilen zurück, ebenfalls liste

print(c.fetchone())  # Gibt die erste Zeile wieder, danach ist diese weg
print(c.fetchmany(2))  # Gibt vorerst nur eine Zeile aus, da nur 2 Stück enthalten sind

# Möglichkeit mehrere Werte in die Datenbank zu speichern:

userList = [
    (3, "abc"),
    (4, "abc"),
    (5, "abc"),
    (6, "abc"),
    (7, "abc"),
    (8, "abc"),
    (9, "abc"),
    (10, "abc")
]

c.executemany("insert into user values (?, ?)", userList)

c.execute("select * from user")

row1 = c.fetchone()
multiple_rows = c.fetchmany(3)
remaining_rows = c.fetchall()

print(row1)
print(multiple_rows)
print(remaining_rows)


# Ist ohne Framework recht mühsam und begrenzt => Empfehlung zu SqlAlchemy

# Damit es weniger fehleranfällig ist, sollte anschließend commited werden und die verbindung geschlossen werden

conn.commit()  # speichert die Daten in der Datenbank
conn.close()  # Trennt die Verbindung zur Datenbank

# Kann auch mit dem context-Manager verwendet werden

with sql.connect("testDatabase.db") as conn:
    c = conn.cursor()
    c.execute("Select * from user")
    print(c.fetchall())

# Mit dem Context Manager wird automatisch nach Ende des Blockes comitted und die Verbindung geschlossen
