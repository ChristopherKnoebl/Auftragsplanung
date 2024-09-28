# Controller-Klasse
from tkinter import messagebox
from model import Lager


class Controller:
    def __init__(self):
        self.lager = Lager()
        

    # Methoden zur Lagerabfrage
    # Von der view erhalten
    def lager_abfragen(self,lagername, ID=0):
        ergebnis = self.lager.lager_abfrage(lagername, ID)
        return ergebnis

    # Methoden zur Lagerdisposition
    # muss noch an das Modell übergeben werden
    def zubuchen_bestand(self, ID, menge):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=}, {menge=} erhalten")

        # muss noch an das Modell übergeben werden
    def ausbuchen_bestand(self, ID, menge):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=}, {menge=} erhalten")
        
    # muss noch an das Modell übergeben werden
    # Methoden für die Auftragsplanung
    def auftrag_abfragen(self, ID):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=} erhalten")

    # Methode für die Auftragserstellung
    # muss noch an das Modell übergeben werden
    def auftrag_erstellen(self, matNr, menge, start, ende):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{matNr=}, {menge=}, {start=}, {ende=} erhalten")
        