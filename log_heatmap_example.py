import matplotlib.pyplot as plt
import numpy as np

# Generiere zufällige Daten, die normalverteilt sind
x = np.random.normal(55000, 10000, size=(1, 10000))
y = np.random.normal(1000, 10000, size=(1, 10000))

# Definiere die Grenzen der Bereiche, in denen die Häufigkeiten der Punkte gezählt werden sollen
# Für die x-Achse eine lineare Verteilung: linspace startet bei 0, endet bei 100000 und teilt diesen Bereich in 20
# gleichgroße Bereiche ein
xedges = np.linspace(0, 100000, 21)

# Für die y-Achse muss der logarithmische Maßstab berücksichtigt werden, deshalb die etwas komplexere Ausführung, aber
# eigentlich analog zur x-Achse. Unteres Limit wählen (hier 10), oberes Limit wählen (hier 100000), Anzahl der Felder
# wählen +1
yedges = np.exp(np.linspace(np.log(10), np.log(100000), 21))

# Damit das Plotten funktioniert, müssen die x-Werte und y-Werte als 1-dimensionales numpy-Array vorliegen.
# Gegebenenfalls mit np.asarray(x) transformieren
plt.hist2d(x[0], y[0], bins=[xedges, yedges])
# Zur Validierung werden als nächstes die originalen Werte geplottet und über die Heatmap gelegt; Heatmap ist aber
# schöner, wenn diese auskommentiert werden
plt.plot(x[0], y[0], 'k.', alpha=0.1)
# Zur Validierung der Grenzen können diese ebenfalls über die folgenden zwei Zeilen geplottet werden; Heatmap ist aber
# # schöner, wenn diese auskommentiert werden
plt.hlines(yedges, 0, 100000)
plt.vlines(xedges, 0, 100000)
# Weitere Feineinstellung für den Plot, die sind dir ja bekannt =)
plt.yscale("log")
plt.ylim(10, 100000)
# Booom! Ergebnis genießen und freuen =)
plt.show()
