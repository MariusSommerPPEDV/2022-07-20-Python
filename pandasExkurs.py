# Pandas ist nicht in Python integriert und muss deshalb erst installiert werden
# Dafür benötigen wir in pycharm das Terminal oder den Reiter Python Packages
# Terminalbefehl:
# pip install <pacakgeName>
# Im Falle von Pandas: pip install pandas

# Damit ich Module verwenden kann, muss ich sie auch importieren

# Hier importiere ich das gesamte Pandas-Modul
# as <kürzel> erlaubt es mir das Modul mit dem Kürzel anzusprechen, statt jedesmal den gesamten Namen zu tippen
import pandas as pd
# Es können auch einzelnen Funktionen oder Klassen aus einem Modul importiert werden
from numpy import sin
# Kann dann nur dei importierte Funktion/Klasse verwenden
# Import kann überall benutzt werden, die importierten Funktionen können aber erst nach dem import statement aufgerufen werden

# Mit pandas eine excel Datei einlesen:

excel_data = pd.read_excel("sampledatahockey.xlsx", sheet_name="PlayerData", header=2)
print(excel_data)

# Hier erstellen wir einen ExcelWriter und benutzen ihn um die Daten in eine neue Excel-Datei zu schreiben
with pd.ExcelWriter("neueExcel.xlsx") as writer:
    excel_data.to_excel(writer)

