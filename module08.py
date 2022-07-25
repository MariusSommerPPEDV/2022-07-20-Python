# Klassen in Python

# Sie sind eine Art Blaupause für Objekte
# Eine Klasse besteht aus Attributen und Methoden
# Methoden sind Funktionen, die zu einem Objekt gehören
# Die Klasse ist nur der abstrakte Gedanke an ein Objekt
# Eine tatsächliche Ausprägung nennen wir Instanz
# Ermöglichen Vererbung
# alle Attribute und Methoden in Python sind public


# Wie definiere ich Klassen:

# Dafür existiert das Keyword class

# Syntax:
# class klassenName():

class Lebewesen():

    # Jede Klasse in Python muss über eine __init__ Funktion verfügen
    # self ist ein Platzhalter für die aufrufende oder zu erstellende Instanz
    # __init__ ist wie ein Constructor anderer Sprachen
    def __init__(self, extremities: int, age: int, species: str):
        self.extremities = extremities  # Attribut der Klasse Lebewesen
        self.age = age  # auch prop genannt
        self.species = species
        self.alive = True

    # Methoden:

    def aging(self):
        print("Lebewesen altert...")
        self.age += 1

    # string Methode
    # Wird aufgerufen, wenn wir es als Text ausgeben lassen wollen
    def __str__(self):
        return f"Es handelt sich um ein Lebewesen der Spezies {self.species}." \
               f" Es ist {self.age} Jahre alt und hat {self.extremities} Extremitäten."


amoeba = Lebewesen(0, 1, "Amoeba")
# __init__(amoeba, ex, age, spec)
#       amoeba.extremities = ex

print(amoeba)
print(amoeba.species)
print(amoeba.age)
amoeba.alive = False
print(amoeba.alive)
amoeba.aging()
print(amoeba.age)
# aging() Geht nicht, da es nur in Kombination mit einer Instanz der Klasse funktioniert
test = f"{amoeba}"  # ruft intern die Funktion __str__ auf
print(test)

# Bei Python-Instanzen können jederzeit neue Attribute hinzugefügt werden
# Diese Props sind Instanzspezifisch und wirken sich nicht auf andere Mitglieder der Klasse aus
amoeba.name = "Ben"  # Dynamisches Attribut, das nur bei amoeba existiert
amoeba.Age = 4  # Legt das neue Attribut Age an, da Python case-sensitive ist

print(amoeba.age)  # behält den alten Wert von 2
print(amoeba.Age)

bacteria = Lebewesen(0, 3, "Bacteria")
print(amoeba.name)
print(bacteria)

# Es können auch Attribute gelöscht werden
# Dafür benutzen wir das del Keyword
# Es wird dabei nicht der Wert der Eigenschaft gelöscht, sonder die gesamte Referenz

del amoeba.Age
del amoeba.name
# print(amoeba.Age) Geht nicht, da das Attribut gelöscht wurde

# del amoeba.age
# print(amoeba.age)
# Es können nicht nur dynamische Props gelöscht werden => Aufpassen

# Vererbung


class Dog(Lebewesen):
    # Es wird ovn der Klasse in der Klammer geerbt
    def __init__(self, age: int, name: str, fur_color: str):
        super().__init__(4, age, "Dog")
        # super() erlaubt es uns den Konstruktor der Elternklasse, hier also Lebewesen aufzurufen
        self.name = name
        self.fur_color = fur_color

    def __str__(self):
        return super().__str__() + f" Der Hund heißt {self.name}. Sein Fell hat eine {self.fur_color} Farbe."


lassie = Dog(5, "Lassie", "golden")

lassie.aging()
print(lassie)
print(lassie.age)

# Python erlaubt multiple Inheritance

# Übung 1 Klassen:
# Erstelle eine Klasse Fahrzeug
# Sie soll über folgende Eigenschaften verfügen:
#   MotoStatus: bool
#   Modell
#   maximaleGeschwindigkeit
#   derzeitigeGeschwindigkeit
#   implementiere die __str__ Methode(Es reicht wenn gesagt wird um welches Modell es sich handelt)
#   Erstelle die Methode Beschleunigen, die einen Paramter akzeptiert
#   Es soll gepürft werden, ob die neue Geschwindigkeit höher ist als die Maximale,
#   falls ja soll der Wert nicht verändert werden


class Fahrzeug:

    def __init__(self, model: str, max_speed: int):
        self.motorStatus = False
        self.model = model
        self.current_speed = 0
        self.max_speed = max_speed

    def __str__(self):
        return f"Es handelt sich um einen {self.model}"

    def accelerate(self, new_speed):
        if new_speed > self.max_speed:
            print("So schnell kann das Fahrzeug nicht fahren.")
        else:
            self.current_speed = new_speed


bmw = Fahrzeug("BMW I3", 150)
print(bmw)
print(bmw.current_speed)
bmw.accelerate(300)
print(bmw.current_speed)
bmw.accelerate(150)
print(bmw.current_speed)
print(bmw.__str__())
bmw_string = f"{bmw}"
