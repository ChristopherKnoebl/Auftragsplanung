import pyodbc

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