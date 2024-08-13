import tkinter
import sqlite3
from tkinter import ttk

def execute_query(connection, sql, params=()):
    """
    Funktion für die Datenbankanbindung
    """
    with connection:
        cursor = connection.cursor()
        cursor.execute(sql, params)
        return cursor.fetchall()


def ermittele_auftragsbedarf(connection, Produkt_Id, Auftragsmenge):

    connection = sqlite3.connect("firma.db")
    cursor = connection.cursor()
    sql = f"""
    Select Materialien.ID, Produkt_Material_Verbund.Menge 
    FROM Produkt_Material_Verbund
    INNER JOIN Produkte on Produkt_Material_Verbund.ProduktID = Produkte.ID 
    Inner JOIN Materialien on Produkt_Material_Verbund.MaterialID = Materialien.ID
    WHERE Produkte.ID =?
    """
    rows = execute_query(connection, sql, (Produkt_Id,))
    material_dictionary = {row[0]: row[1] * Auftragsmenge for row in rows}
    return material_dictionary


  

def ermittle_lagerbestand(connection, dictionary_auftragsbedarf):
    """
    Funktion, mit der der Lagerbestand für einen gegebenen Auftrag berechnet wird
    """
    lagerbestand = {}
    for k in dictionary_auftragsbedarf.keys():
        sql = """
        SELECT Lagerbestand.MaterialID, SUM(Lagerbestand.Menge)
        FROM Lager
        INNER JOIN Lagerbestand ON Lagerbestand.LagerID = Lager.ID
        WHERE Lagerbestand.MaterialID = ?
        """
        rows = execute_query(connection, sql, (k,))
        for row in rows:
            lagerbestand[row[0]] = row[1]
    return lagerbestand

def vergleiche_bedarf_bestand(dictionary_auftragsbedarf, dictionary_lagerbestand):
    for k in dictionary_auftragsbedarf.keys():
        if dictionary_auftragsbedarf[k] > dictionary_lagerbestand.get(k, 0):
            return False
    return True

# öffne das Hauptfenster
main = tkinter.Tk()
navigations_frame = tkinter.Frame(main)
navigations_frame.grid(row=0, column=0)

eingabe_frame = tkinter.Frame(main)
eingabe_frame.grid(row=1, column=0)

ausgabe_frame = tkinter.Frame(main)
ausgabe_frame.grid(row=2, column=0)

# Funktion um ein bereits erstellten Frame zu löschen
def loesche_frame(fenster):
    for widget in fenster.winfo_children():
        widget.destroy()

# öffnet ein neues Fenster, in dem ein Fertigungsauftrag erstellt werden kann
def oeffne_auftragserstellung():
    """
    Mit dieser Funktion wird ein neuer Frame erstellt, in dem Aufträge eingegeben werden können
    """

    # leert das Fenster bevor ein neues aufgebaut wird
    loesche_frame(eingabe_frame)
    loesche_frame(ausgabe_frame)

    def erstelle_auftrag():
        """
         Eingabe: Werte, die in die Entry-Widgets eingegeben wurden
         Verarbeitung: Mit diesen Werten wird die Tabelle "Fertigungsaufträge" befüllt
         Ausgabe: Meldung, falls ein Feld nicht ausgefüllt wurde, ansonsten "Auftrag erstellt"
        """

        try:
            ProduktID = int(etProduktID.get())
            Menge = int(etMenge.get())
            Anfangsdatum = str(etAnfangdatum.get())
            Enddatum = etEnddatum.get()
            lbAusgabe["text"] = "Auftrag erstellt"
        except:
            lbAusgabe["text"] = "Bitte alle Felder ausfüllen"
        finally:
            if len(Anfangsdatum) == 0 or len(Enddatum) == 0:
                lbAusgabe["text"] = "Bitte alle Felder ausfüllen"
                erstelle_auftrag()

        etProduktID.delete(0, 'end')
        etMenge.delete(0, 'end')
        etAnfangdatum.delete(0, 'end')
        etEnddatum.delete(0, 'end')
        connection = sqlite3.connect("firma.db")
        sql_script = """
            INSERT INTO Fertigungsaufträge (ProduktID, Menge, Auftragsbeginn, Auftragsende)
            VALUES (?, ?, ?, ?)
            """
        execute_query(connection, sql_script, (ProduktID, Menge, Anfangsdatum, Enddatum))
        connection.commit()

        auftragsbedarf = ermittele_auftragsbedarf(connection, ProduktID, Menge)
        lagerbestand = ermittle_lagerbestand(connection, auftragsbedarf)

        if vergleiche_bedarf_bestand(auftragsbedarf, lagerbestand) == True:
            lbAuftragMöglich["text"] = "Der Auftrag kann erstellt werden"
        else:
            lbAuftragMöglich["text"] = "Für den Auftrag fehlt noch Material"
        
        

    lbProdukt = tkinter.Label(eingabe_frame, text="Produkt-ID:")
    lbProdukt.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    etProduktID = tkinter.Entry(eingabe_frame)
    etProduktID.grid(row=0, column=1, padx=5, pady=5)

    lbMenge = tkinter.Label(eingabe_frame, text="Menge:")
    lbMenge.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    etMenge = tkinter.Entry(eingabe_frame)
    etMenge.grid(row=1, column=1, padx=5, pady=5)

    lbAnfangdatum = tkinter.Label(eingabe_frame, text="Auftragsbeginn:")
    lbAnfangdatum.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    etAnfangdatum = tkinter.Entry(eingabe_frame)
    etAnfangdatum.grid(row=2, column=1, padx=5, pady=5)

    lbEnddatum = tkinter.Label(eingabe_frame, text="Auftragsende")
    lbEnddatum.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    etEnddatum = tkinter.Entry(eingabe_frame)
    etEnddatum.grid(row=3, column=1, padx=5, pady=5)

    lbAusgabe = tkinter.Label(ausgabe_frame, text="Auftrag-Erstellen")
    lbAusgabe.grid(row=4, column=0, padx=5, pady=5)

    buAuftragErstellen = tkinter.Button(eingabe_frame, text="Erstelle Auftrag", command=erstelle_auftrag)
    buAuftragErstellen.grid(row=4, column=1, padx=5, pady=5)

    lbAuftragMöglich = tkinter.Label(eingabe_frame, text="Prüfe, ob Auftrag erstellt werden kann.")
    lbAuftragMöglich.grid(row=4, column=2, padx=5, pady=5)

buFenster = ttk.Button(main, text="Auftrag erstellen", command=oeffne_auftragserstellung)
buFenster.grid(row=0, column=0, padx=5, pady=5)


# öffnet ein neues Fenster, in dem die verschiedenen Tabellen abgefragt werden können
def oeffneTabellenbfrage():

    # leert das Fenster bevor ein neues aufgebaut wird
    loesche_frame(eingabe_frame)
    loesche_frame(ausgabe_frame)

    def abfrage():
        """
        gibt die eingegebene Tabelle in der Form einer Treeview wieder aus
        """

        try:
            tabelle = str(etEingabe.get())

            # Define a whitelist of allowed table names
            allowed_tables = ["Produkte", "Materialien", "Fertigungsaufträge", "Lagerbestand", "Lager"]

            if tabelle not in allowed_tables:
                lbTabelle["text"] = "Ungültige Tabelle ausgewählt"
                return

            # Proceed with the query now that `tabelle` is validated
            sql = f"SELECT * FROM {tabelle}"  # Safe since `tabelle` is validated against the whitelist
            cursor.execute(sql)
        except:
            lbTabelle["text"] = f"{tabelle}"


        connection = sqlite3.connect("firma.db")
        cursor = connection.cursor()
        sql = f"Select * FROM {tabelle}"
        cursor.execute(sql)

        anzahl_spalten = 0

        sql = f"""
        select count(*) from pragma_table_info('{tabelle}');
        """
        cursor.execute(sql)

        for i in cursor:
            anzahl_spalten = i[0]

        trv = ttk.Treeview(ausgabe_frame, selectmode='browse')
        trv.grid(row=1, column=1, padx=20, pady=20)

        liste_der_spalten = []  # hilfstabelle, um die Spaltendarzustellen
        # number of columns
        for i in range(1, anzahl_spalten + 1):
            liste_der_spalten.append(str(i))

        tuple_anzahl_spalten = tuple(liste_der_spalten)
        trv["columns"] = tuple_anzahl_spalten

        # Defining heading
        trv['show'] = 'headings'

        # # width of columns and alignment 
        for i in liste_der_spalten:
            if i == "1":
                trv.column(i, width=20, anchor='c')
            else:
                trv.column(i, width=80, anchor='c')

        # Headings  
        # respective columns

        sql = f"""
        pragma table_info('{tabelle}');
        """
        cursor.execute(sql)

        dict_tabelle = {}  # hilfsdictionary um den Spalten die Bezeichnung zuzuordnen
        for i in cursor:
            dict_tabelle[str(i[0] + 1)] = i[1]
        print(dict_tabelle)
        for k, v in dict_tabelle.items():
            trv.heading(k, text=v)
        connection = sqlite3.connect("firma.db")
        cursor = connection.cursor()
        sql = f"Select * FROM '{tabelle}'"
        cursor.execute(sql)
        trv.tag_configure('gray', background='lightgray')
        trv.tag_configure('normal', background='white')
        my_tag = 'normal'  # default value
        values_list = []  # hilfsliste, um die werte eintragen zu können

        # holt die Werte für die Ausgabe aus der Datenbank
        for dt in cursor:
            values_list = []  # hilfsliste, um die werte eintragen zu können
            for i in range(len(liste_der_spalten)):
                values_list.append(dt[i])

            values_tupel = tuple(values_list)
            my_tag = 'gray' if my_tag == 'normal' else 'normal'
            trv.insert("", 'end', iid=dt[0], text=dt[0],
                       #    values =(dt[0],dt[1], dt[2], dt[3], dt[4]),tags=(my_tag))
                       values=values_tupel, tags=(my_tag))
        connection.commit()

    lbEingabe = tkinter.Label(eingabe_frame, text="Ihre Eingabe:")
    lbEingabe.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    etEingabe = tkinter.Entry(eingabe_frame)
    etEingabe.grid(row=1, column=0, padx=5, pady=5)

    buAbfragen = tkinter.Button(eingabe_frame, text="Abfragen", command=abfrage, width=10)
    buAbfragen.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    lbAusgabe = tkinter.Label(eingabe_frame, text="")
    lbAusgabe.grid(row=3, column=0, sticky="w", padx=5, pady=5)

    lbTabelle = tkinter.Label(eingabe_frame, text="")
    lbTabelle.grid(row=0, column=1, padx=5, pady=5)


buFenster = ttk.Button(main, text="Tabelle abfragen", command=oeffneTabellenbfrage)
buFenster.grid(row=0, column=1, padx=5, pady=5)

tkinter.mainloop()
