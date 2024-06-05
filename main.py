import tkinter
import sqlite3
from tkinter import ttk

#öffne das Hauptfenster
main = tkinter.Tk()

# erstell
def oeffneAuftragsErstellung():
    """
    Mit dieser Funktion wird ein neues Fenster erstellt, in dem Aufträge eingegebenw werden können
    """
    FensterAuftragserstellung = tkinter.Toplevel(main)
    FensterAuftragserstellung.title("Auftrag erstellen")

    lbProdukt = tkinter.Label(FensterAuftragserstellung, text="Produkt-ID:")
    lbProdukt.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    etProduktID = tkinter.Entry(FensterAuftragserstellung)
    etProduktID.grid(row=0, column=1, padx=5, pady=5)

    lbMenge = tkinter.Label(FensterAuftragserstellung, text="Menge:")
    lbMenge.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    etMenge = tkinter.Entry(FensterAuftragserstellung)
    etMenge.grid(row=1, column=1, padx=5, pady=5)

    lbAnfangdatum = tkinter.Label(FensterAuftragserstellung, text="Auftragsbeginn:")
    lbAnfangdatum.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    etAnfangdatum = tkinter.Entry(FensterAuftragserstellung)
    etAnfangdatum.grid(row=2, column=1, padx=5, pady=5)

    lbEnddatum = tkinter.Label(FensterAuftragserstellung, text="Auftragsende")
    lbEnddatum.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    etEnddatum = tkinter.Entry(FensterAuftragserstellung)
    etEnddatum.grid(row=3, column=1, padx=5, pady=5)

    lbAusgabe = tkinter.Label(FensterAuftragserstellung, text="Auftrag-Erstellen")
    lbAusgabe.grid(row=4, column=0, padx=5, pady=5)
    
    buAuftragErstellen = tkinter.Button(FensterAuftragserstellung, text ="Erstelle Auftrag")
    buAuftragErstellen.grid(row=4, column=1, padx=5, pady=5)

buFenster = ttk.Button(main, text="Auftrag erstellen", command=oeffneAuftragsErstellung)
buFenster.grid(row=0, column=0, padx=5, pady=5)

def oeffneTabellenbfrage():
    Tabellenabfrage = tkinter.Toplevel(main)
    Tabellenabfrage.title("Tabelle abfragen")

    lbEingabe = tkinter.Label(Tabellenabfrage, text="Ihre Eingabe:")
    lbEingabe.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    etEingabe = tkinter.Entry(Tabellenabfrage)
    etEingabe.grid(row=1, column=0, padx=5, pady=5)

    buAbfragen = tkinter.Button(Tabellenabfrage, text="Abfragen", width=10)
    buAbfragen.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    lbAusgabe = tkinter.Label(Tabellenabfrage, text="")
    lbAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

    lbTabelle = tkinter.Label(Tabellenabfrage, text="")
    lbTabelle.grid(row=0, column=1, padx=5, pady=5)

buFenster = ttk.Button(main, text="Tabelle abfragen", command=oeffneTabellenbfrage)
buFenster.grid(row=0, column=1, padx=5, pady=5)

tkinter.mainloop()
