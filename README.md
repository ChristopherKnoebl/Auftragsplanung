# Auftragsplanung
Eine kleine Anwendung mit der Aufträge und Lagerbestände organisiert werden können.

## Idee
Es ist teilweise ärgerlich, wenn Fertigungsaufträge freigegeben werden, ohne dass für diese ausreichend Material im Lager vorrätig ist. Diese Anwendung überprüft den Lagerbestand bevor ein Auftrag freigegeben wird und liefert eine Rückmeldung.

## Zur neuen Version
Der alte Softwarestand ist im Order "Alter Stand" zu finden. An diesem Code wird nicht weiter gearbeitet. Das Projekt wird von Grund auf neu überarbeitet und geplant.

## Use Cases
Das Programm kümmert sich aktuell um zwei Use Cases:
1. Auftragserstellung
- Es können Fertigungsaufträge in der Datenbank abgespeichert werden. Hierbei wird zugleich eine Abfrage unternommen, ob genug Material vorhanden ist und bei negativem Resultat wird eine Warnung ausgegeben.
- Beim Abspeichern des Fertigungsauftrages wird ein timestamp erstellt.
2. Materialdisposition
- In der Tabelle Material kann Material gespeichert oder gelöscht werden.

Perspektivisch werden weitere Use Cases behandelt werden:
1. Es wird eine Rollenverteilung mit Mitarbeiter, Steuerer und Disponent geben.
2. Bei Erstellung eines Fertigungsauftrages wird das benötigte Material automatisch reserviert.

## Projektverlauf
Das Grundgerüst für das Programm ist entworfen. Da mittelfristig ein anderes Framework für die GUI verwendet werden soll wird die Anwendung nach dem Model-View-Controller-Musters entworfen. In diesem Zusammenhang erscheint es günstig die Programmrierung nach dem objektorientierten Paradigma zu gestalten.

### Die View und der Controller
Eine überarbeitete Version der View ist erstellt. Hierbei werden die einzelnen Fenster als Klassen entworfen, welche mit tkinter grafisch dargestellt werden. Zu Testzecken wird die Nutzereingagbe im Feld "Rueck" dargestellt. Diese Behelfslösung wird entfernt, sobald Controller und Model entwickelt sind.
###
Derzeit wird der Controller entwickelt. In einem ersten Schritt soll dieser die Eingaben des Users aufnehmen und wieder auf die GUI zurückgeben. Nach Fertigstellugn des Modells gibt der Controller die Eingabn zur weiteren Verarbeitung an das Modell weiter.
### Das Modell
Ein erster Entwurf der Datenbank steht. Als nächstes werden die Klassen für das Lager und die Fertigungsaufträge erstellt.
