import tkinter as tk
from tkinter import messagebox

# Klasse Fertigungsaufträge (bleibt unverändert)
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

# Controller-Klasse
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

# Hauptfenster-Klasse wird zur Elternklasse
class Hauptfenster:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller  # Speichere den Controller
        self.root.title("Auftragsmanagement")

        # Buttons im Hauptfenster
        self.button_bestandsabfrage = tk.Button(root, text="Bestandsabfrage", command=self.oeffne_bestandsabfrage)
        self.button_bestandsabfrage.pack()

        self.button_auftragsabfrage = tk.Button(root, text="Auftragsabfrage", command=self.oeffne_auftragsabfrage)
        self.button_auftragsabfrage.pack()

        self.button_bestandsdisposition = tk.Button(root, text="Bestandsdisposition", command=self.oeffne_bestandsdisposition)
        self.button_bestandsdisposition.pack()

        self.button_auftragserstellung = tk.Button(root, text="Auftragserstellung", command=self.oeffne_auftragserstellung)
        self.button_auftragserstellung.pack()

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
        self.button_bestand_abfragen = tk.Button(self.window, text="Bestand abfragen", command=self.frage_bestand_ab)
        self.button_bestand_abfragen.pack()

        self.button_fenster_schließen = tk.Button(self.window, text="Fenster schließen", command=self.schliesse_fenster)
        self.button_fenster_schließen.pack()

    def frage_bestand_ab(self):
        print("Bestand wird abgefragt...")
        messagebox.showinfo("Bestandsabfrage", "Der Bestand wurde abgefragt.")

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
