import tkinter as tk
from tkinter import messagebox
import pyodbc

# Klassen aus dem Model
# Klasse Fertigungsaufträge 
class Fertigungsauftraege:
    def __init__(self, auftragsnummer, produktname, menge, auftragsbeginn, auftragsende):
        self.auftragsnummer = auftragsnummer
        self.produktname = produktname
        self.menge = menge
        self.auftragsbeginn = auftragsbeginn
        self.auftragsende = auftragsende
        self.timestamp = None

    def kalkuliere_materialbedarf(self):
        print("Materialbedarf wird kalkuliert...")

    def erstelle_stueckliste(self):
        print("Stückliste wird erstellt...")

    def deckt_lagerbestand_materialbedarf(self):
        print("Prüfe, ob der Lagerbestand den Materialbedarf deckt...")

# Klasse Lager
class Lager():
    SERVER = 'Chris-PC'
    DATABASE = 'Beispiel-Firma'
    USERNAME = '<username>'
    PASSWORD = '<password>'

    def __init__(self, name) -> None:
        self.name = name

    def lager_abfrage(self, ID=0):
        connectionString = f"""
        DRIVER={{ODBC Driver 18 for SQL Server}};
        SERVER={Lager.SERVER};
        DATABASE={Lager.DATABASE};
        Trusted_Connection=yes;
        TrustServerCertificate=yes;
"""
        try:
            # Datenbankanbindung
            conn = pyodbc.connect(connectionString)
            cursor = conn.cursor()
            print("Verbindung hergestellt")
            if ID == 0:
                SQL = f"""
                SELECT * FROM [Beispiel-Firma].[dbo].[{self.name}];
                """
                print(f"{ID=}")
                cursor.execute(SQL)
            else:
                SQL = f"""
                SELECT * FROM [Beispiel-Firma].[dbo].[{self.name}]
                WHERE ID = 1;
                """
                cursor.execute(SQL)

            ergebnisse = []
            records = cursor.fetchall()
            for r in records:
                ergebnisse.append(r)
            print(ergebnisse)
            
        except pyodbc.Error as e:
            print(f"Fehler bei der Datenbankverbindung: {e}")
        finally:
            cursor.close()
            conn.close()
        return f"{ergebnisse=}"
model1 = Lager("Materialien")
print(model1.lager_abfrage())

# Controller-Klasse
class LagerController :
    def __init__(self) -> None:
        pass

class AuftragsController:
    def __init__(self):
        self.auftraege = []  # Liste von Fertigungsaufträgen

    def erstelle_auftrag(self, auftragsnummer, produktname, menge, auftragsbeginn, auftragsende):
        auftrag = Fertigungsauftraege(auftragsnummer, produktname, menge, auftragsbeginn, auftragsende)
        self.auftraege.append(auftrag)
        print(f"Auftrag {auftragsnummer} erstellt: {produktname}, Menge: {menge}")
        return auftrag

    def frage_auftrag_ab(self, auftragsnummer):
        for auftrag in self.auftraege:
            if auftrag.auftragsnummer == auftragsnummer:
                print(f"Auftrag {auftragsnummer} gefunden: {auftrag.produktname}")
                return auftrag
        print(f"Auftrag {auftragsnummer} nicht gefunden.")
        return None

    def frage_bestand_ab(self):
        print("Bestand wird abgefragt...")
        return {"Produkt A": 100, "Produkt B": 50}

    def disponiere_bestand(self):
        print("Bestand wird disponiert...")
        return True

# Klassen aus der GUI
# Hauptfenster-Klasse wird zur Elternklasse
class Hauptfenster:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller  # Speichere den Controller
        self.root.title("Auftragsmanagement")

        # Buttons im Hauptfenster
        self.button_bestandsabfrage = tk.Button(root, text="Bestandsabfrage", command=self.oeffne_bestandsabfrage)
        self.button_bestandsabfrage.pack(side="left")

        self.button_auftragsabfrage = tk.Button(root, text="Auftragsabfrage", command=self.oeffne_auftragsabfrage)
        self.button_auftragsabfrage.pack(side="left")

        self.button_bestandsdisposition = tk.Button(root, text="Bestandsdisposition", command=self.oeffne_bestandsdisposition)
        self.button_bestandsdisposition.pack(side="left")

        self.button_auftragserstellung = tk.Button(root, text="Auftragserstellung", command=self.oeffne_auftragserstellung)
        self.button_auftragserstellung.pack(side="left")

    # Methode zum Öffnen der verschiedenen Fenster
    def oeffne_bestandsabfrage(self):
        Bestandsabfrage(self.root, self.controller)

    def oeffne_auftragsabfrage(self):
        Auftragsabfrage(self.root, self.controller)

    def oeffne_bestandsdisposition(self):
        Bestandsdisposition(self.root, self.controller)

    def oeffne_auftragserstellung(self):
        Auftragserstellung(self.root, self.controller)

# Kindklassen, die von Hauptfenster erben, aber das Hauptfenster nicht verändern
class Bestandsabfrage(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Bestandsabfrage")

        # Widgets in Bestandsabfrage-Fenster
        self.label_anfrage = tk.Label(self.window, text="Welches Lager soll abgefragt werden?")
        self.label_anfrage.grid(row=0, columnspan=2)

        self.button_materialien = tk.Button(self.window, text="Materiallager", command=lambda:self.setze_lager("Materialien"))
        self.button_materialien.grid(row=1, column=0, padx=5, pady=5)

        self.button_produkte = tk.Button(self.window, text="Produktlager", command=lambda:self.setze_lager("Produkte"))
        self.button_produkte.grid(row=1, column=1, padx=5, pady=5)

        self.label_eingabe = tk.Label(self.window, text="Kein Lager")
        self.label_eingabe.grid(row=2, column=0, padx=5, pady=5)

        self.entry_lager = tk.Entry(self.window)
        self.entry_lager.grid(row=2, column=1, padx=5, pady=5)

        self.button_abfragen = tk.Button(self.window, text="Abfragen", command= self.gib_rueck) 
        self.button_abfragen.grid(row=2,column=2, padx=5, pady=5)

        self.label_rueckgabe = tk.Label(self.window, text="Rückgabe")
        self.label_rueckgabe.grid(row=2,column=3, padx=5, pady=5)
    # Hilfsmethode zur Auswahl des Lagers
    def setze_lager(self, lagername):
        self.lagername = lagername
        self.label_eingabe["text"] = f"ID eingeben: "
        print(self.lagername)
    
    def gib_rueck(self):
        lagername = self.lagername, 
        menge = int(self.entry_lager.get())
        # ergebnis = controller.lager_abfragen(lagername, menge)    # methode muss noch im controller bearbeitet werden
        self.label_rueckgabe["text"] = f"{lagername=}, {menge=}"

class Bestandsdisposition(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Bestandsdisposition")

        # Widgets in Bestandsdisposition-Fenster
        self.label_anfrage = tk.Label(self.window, text="Welches Material soll disponiert werden?")
        self.label_anfrage.grid(row=0, columnspan=2, padx=5, pady=5)

        self.label_material = tk.Label(self.window, text="Materialnummer")
        self.label_material.grid(row=1, column=0, padx=5, pady=5)

        self.entry_material = tk.Entry(self.window)
        self.entry_material.grid(row=1, column=1, padx=5, pady=5)

        self.label_menge = tk.Label(self.window, text="Menge")
        self.label_menge.grid(row=2, column=0, padx=5, pady=5)

        self.entry_menge = tk.Entry(self.window)
        self.entry_menge.grid(row=2, column=1, padx=5, pady=5)       

        self.button_bestand_zubuchen = tk.Button(self.window, text="Bestand zubuchen", \
        command=self.zubuchen_bestand)
        self.button_bestand_zubuchen.grid(row=2,column=2, padx=5, pady=5)  

        self.button_bestand_ausbuchen = tk.Button(self.window, text="Bestand ausbuchen", command=self.abbuchen_bestand)
        self.button_bestand_ausbuchen.grid(row=3,column=2, padx=5, pady=5)  

        self.label_rueck = tk.Label(self.window, text="Rückgabe")
        self.label_rueck.grid(row=3,column=3, padx=5, pady=5)  

    # Methoden zur Bestandsdisposition
        
    def zubuchen_bestand(self):
        ID = int(self.entry_material.get())
        menge = int(self.entry_menge.get())
        self.label_rueck["text"] = f"{ID=}, {menge=}"
        return ID, menge
    
    def abbuchen_bestand(self):
        ID = int(self.entry_material.get())
        menge = int(self.entry_menge.get()) * (-1)
        self.label_rueck["text"] = f"{ID=}, {menge=}"
        return ID, menge

class Auftragsabfrage(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Auftragsabfrage")
        self.controller = controller

        # Widgets in Auftragsabfrage-Fenster
        self.label_fertigungsauftrag = tk.Label(self.window, text="Auftragsnummer")
        self.label_fertigungsauftrag.grid(row=1, column=0, padx=5, pady=5)

        self.entry_fertigungsauftrag = tk.Entry(self.window)
        self.entry_fertigungsauftrag.grid(row=1, column=1, padx=5, pady=5)

        self.button_auftrag_abfragen = tk.Button(self.window, text="Auftrag abfragen", command= self.frage_auftrag_ab)
        self.button_auftrag_abfragen.grid(row=2, column=1, padx=5, pady=5)

        self.label_rueck = tk.Label(self.window, text="Rückgabe")
        self.label_rueck.grid(row=3,column=3, padx=5, pady=5)  

    # Methode, um die Fertigungaufträge abzufragen
    def frage_auftrag_ab(self):
        ID = int(self.entry_fertigungsauftrag.get())
        self.label_rueck["text"] = f"{ID=}"
        return ID

class Auftragserstellung(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Auftragserstellung")
        self.controller = controller  # Controller-Referenz

        # Widgets in Auftragserstellung-Fenster
        self.label_material = tk.Label(self.window, text="Materialnummer")
        self.label_material.grid(row=1, column=0, padx=5, pady=5)

        self.entry_material = tk.Entry(self.window)
        self.entry_material.grid(row=1, column=1, padx=5, pady=5)

        self.label_menge = tk.Label(self.window, text="Auftragsmenge")
        self.label_menge.grid(row=2, column=0, padx=5, pady=5)

        self.entry_menge = tk.Entry(self.window)
        self.entry_menge.grid(row=2, column=1, padx=5, pady=5)

        self.label_beginn = tk.Label(self.window, text="Auftragsbeginn")
        self.label_beginn.grid(row=3, column=0, padx=5, pady=5)

        self.entry_beginn = tk.Entry(self.window)
        self.entry_beginn.grid(row=3, column=1, padx=5, pady=5)

        self.label_ende = tk.Label(self.window, text="Auftragsende")
        self.label_ende.grid(row=4, column=0, padx=5, pady=5)

        self.entry_ende = tk.Entry(self.window)
        self.entry_ende.grid(row=4, column=1, padx=5, pady=5)

        self.button_auftrag_erstellen = tk.Button(self.window, text="Auftrag erstellen", command=self.erstelle_auftrag)
        self.button_auftrag_erstellen.grid(row=5, column=0, padx=5, pady=5)

        self.label_rueck = tk.Label(self.window, text="Rückgabe")
        self.label_rueck.grid(row=6,column=0, padx=5, pady=5) 

    def erstelle_auftrag(self):
        matNr = int(self.entry_material.get())
        menge = int(self.entry_menge.get())
        start = self.entry_beginn.get()
        ende = self.entry_ende.get()
        self.label_rueck["text"] = f"{matNr=}, {menge=}, {start=}, {ende=}"
        return matNr, menge, start, ende

# Main-Loop
if __name__ == "__main__":
    root = tk.Tk()
    controller = AuftragsController()
    app = Hauptfenster(root, controller)
    root.mainloop()
