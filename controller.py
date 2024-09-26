# Controller-Klasse
from tkinter import messagebox
from model import Lager

class Controller:
    def __init__(self):
        pass

    # Methoden zur Lagerabfrage
    # Von der view erhalten
    def lager_abfragen(self,lagername, ID=0):
        # lager = Lager(lagername)
        # lager.lager_abfrage(ID)
        return lagername, ID
    # muss noch durchgeprüft werden, Anschluss an Datenbank notwendig
    # return muss noch an das modell weiter gegeben werden

    # Methoden zur Lagerdisposition
    def zubuchen_bestand(self, ID, menge):
        pass
    #     lager = Lager("Materialien")
    #     ID = self.entry_material.get()
    #     menge = int(self.entry_menge.get())
    #     lager.material_erhöhen(ID, menge)
    #     return ID, menge
    
    def ausbuchen_bestand(self, ID, menge):
        pass
    #     lager = Lager("Materialien")
    #     ID = self.entry_material.get()
    #     menge = int(self.entry_menge.get())
    #     lager.material_reduzieren(ID, menge)
    #     return ID, menge
        
    
    # Methoden für die Auftragsplanung
    def auftrag_abfragen(self, ID):
        messagebox.showinfo("Der Controller hat die Anfrage:", f"{ID=} erhalten")
        
