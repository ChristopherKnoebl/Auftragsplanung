import pyodbc

# Klasse Fertigungsaufträge 
class Fertigungsauftraege:
    # muss noch implementiert werden
    pass
# Klasse Lager
class Lager():
    SERVER = 'Chris-PC'
    DATABASE = 'Beispiel-Firma'
    USERNAME = '<username>'
    PASSWORD = '<password>'

    def __init__(self) -> None:
        pass

    def lager_abfrage(self,lagername, ID=0):
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
                SELECT * FROM [Beispiel-Firma].[dbo].[{lagername}];
                """
                cursor.execute(SQL)
            else:
                SQL = f"""
                SELECT * FROM [Beispiel-Firma].[dbo].[{lagername}]
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
# model1 = Lager()
# print(model1.lager_abfrage("Materialien", 1))
