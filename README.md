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
Das Grundgerüst für das Programm ist entworfen. Da die User mittels der GUI auf die Datenbank zugreifen können wird die Anwendung in der Art des Model-View-Controller-Musters entworfen. In diesem Zusammenhang erscheint es günstig die Programmrierung nach dem objektorientierten Paradigma zu gestalten.

### Die View und der Controller
Eine erste Version der View ist erstellt. Hierbei werden die einzelnen Fenster als Klassen entworfen, welche mit tkinter grafisch dargestellt werden. Da das Model noch entwickelt wird, gibt die View zu diesem Zeitpunkt ihre Befehle nur an den Controller weiter, welcher eine Rückgabe auf das Terminal liefert und einen Default-Fertigungsauftrag wiedergibt.

### Das Modell
Die zugrunde liegende Datenbank wird in MSSQL entwickelt, die Prozesslogik wird wird durch eigene Klassen nachgestellt. 