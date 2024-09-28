# Controller-Klasse
from tkinter import messagebox
from model import Lager

class Controller:
    def __init__(self):
        pass

    # Methoden zur Lagerabfrage
    # Von der view erhalten
    # müssen noch an das Modell übergeben werden
    def lager_abfragen(self,lagername, ID=0):

        messagebox.showinfo("Der Controller hat die Anfrage:", f"{lagername=}, {ID=} erhalten")
    # muss noch durchgeprüft werden, Anschluss an Datenbank notwendig
    # return muss noch an das modell weiter gegeben werden

    # Methoden zur Lagerdisposition
    def zubuchen_bestand(self, ID, menge):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=}, {menge=} erhalten")

    def ausbuchen_bestand(self, ID, menge):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=}, {menge=} erhalten")
        
    
    # Methoden für die Auftragsplanung
    def auftrag_abfragen(self, ID):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=} erhalten")

    # Methode für die Auftragserstellung

    def auftrag_erstellen(self, matNr, menge, start, ende):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{matNr=}, {menge=}, {start=}, {ende=} erhalten")
        