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
        self.controller = controller

        # Widgets in Bestandsabfrage-Fenster
        self.button_materialien_abfragen = tk.Button(self.window, text="Material-Bestand abfragen", command=self.frage_material_ab)
        self.button_materialien_abfragen.pack()

        self.button_produkte_abfragen = tk.Button(self.window, text="Produkt-Bestand abfragen", command=self.frage_produkt_ab)
        self.button_produkte_abfragen.pack()

        self.button_fenster_schließen = tk.Button(self.window, text="Fenster schließen", command=self.schliesse_fenster)
        self.button_fenster_schließen.pack()

    def frage_material_ab(self, ID=0):
        lager = Lager("Materialien")
       
        print("Bestand wird abgefragt...")
        messagebox.showinfo("Bestandsabfrage", f"{lager.lager_abfrage(ID)}.")

        return lager.lager_abfrage(ID)
    
    def frage_produkt_ab(self, ID=0):
        lager = Lager("Produkte")
       
        print("Bestand wird abgefragt...")
        messagebox.showinfo("Bestandsabfrage", f"{lager.lager_abfrage(ID)}.")

        return lager.lager_abfrage(ID)

    # Methode zum Schließen des Fensters
    def schliesse_fenster(self):
        self.window.destroy()

class Bestandsdisposition(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Bestandsdisposition")
        self.controller = controller

        # Widgets in Bestandsdisposition-Fenster
        self.button_bestand_disponieren = tk.Button(self.window, text="Bestand disponieren", command=self.disponiere_bestand)
        self.button_bestand_disponieren.pack()

        self.button_bestand_abfragen = tk.Button(self.window, text="Bestand abfragen", command=self.frage_bestand_ab)
        self.button_bestand_abfragen.pack()

        self.button_fenster_schließen = tk.Button(self.window, text="Fenster schließen", command=self.schliesse_fenster)
        self.button_fenster_schließen.pack()

    def frage_bestand_ab(self):
        print("Bestand wird abgefragt...")
        messagebox.showinfo("Bestandsabfrage", "Der Bestand wurde abgefragt.")

    def disponiere_bestand(self):
        print("Bestand wird disponiert...")
        messagebox.showinfo("Bestandsdisposition", "Der Bestand wurde disponiert.")

    # Methode zum Schließen des Fensters
    def schliesse_fenster(self):
        self.window.destroy()

class Auftragsabfrage(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Auftragsabfrage")
        self.controller = controller

        # Widgets in Auftragsabfrage-Fenster
        self.button_auftrag_abfragen = tk.Button(self.window, text="Auftrag abfragen", command=self.frage_auftrag_ab)
        self.button_auftrag_abfragen.pack()

        self.button_fenster_schließen = tk.Button(self.window, text="Fenster schließen", command=self.schliesse_fenster)
        self.button_fenster_schließen.pack()

    def frage_auftrag_ab(self):
        print("Auftrag wird abgefragt...")
        messagebox.showinfo("Auftragsabfrage", "Der Auftrag wurde abgefragt.")

    # Methode zum Schließen des Fensters
    def schliesse_fenster(self):
        self.window.destroy()

class Auftragserstellung(Hauptfenster):
    def __init__(self, master, controller):
        self.window = tk.Toplevel(master)  # Neues Fenster
        self.window.title("Auftragserstellung")
        self.controller = controller  # Controller-Referenz

        # Widgets in Auftragserstellung-Fenster
        self.button_auftrag_erstellen = tk.Button(self.window, text="Auftrag erstellen", command=self.erstelle_auftrag)
        self.button_auftrag_erstellen.pack()

        self.button_auftrag_abfragen = tk.Button(self.window, text="Auftrag abfragen", command=self.frage_auftrag_ab)
        self.button_auftrag_abfragen.pack()

        self.button_fenster_schließen = tk.Button(self.window, text="Fenster schließen", command=self.schliesse_fenster)
        self.button_fenster_schließen.pack()

    def erstelle_auftrag(self):
        # Hier könnte der Nutzeraufgabeparameter über Eingabefelder erfasst werden
        self.controller.erstelle_auftrag(123, "Produkt X", 10, "2023-09-01", "2023-09-05")
        messagebox.showinfo("Auftragserstellung", "Ein Auftrag wurde erstellt.")

    def frage_auftrag_ab(self):
        auftrag = self.controller.frage_auftrag_ab(123)
        if auftrag:
            messagebox.showinfo("Auftragsabfrage", f"Auftrag gefunden: {auftrag.produktname}")
        else:
            messagebox.showinfo("Auftragsabfrage", "Auftrag nicht gefunden.")

    # Methode zum Schließen des Fensters
    def schliesse_fenster(self):
        self.window.destroy()

# Main-Loop
if __name__ == "__main__":
    root = tk.Tk()
    controller = AuftragsController()
    app = Hauptfenster(root, controller)
    root.mainloop()

