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
    
    def zubuchen(self, ID, menge):
        connectionString = f"""
        DRIVER={{ODBC Driver 18 for SQL Server}};
        SERVER={Lager.SERVER};
        DATABASE={Lager.DATABASE};
        Trusted_Connection=yes;
        TrustServerCertificate=yes;
        """
        try:
            conn = pyodbc.connect(connectionString)
            cursor = conn.cursor()
            print("Verbindung zum Lager hergestellt")

            SQL = f"""
            UPDATE [Beispiel-Firma].[dbo].[Materialien]
            SET Menge = Menge + ?
            WHERE ID = ?;
            """
            cursor.execute(SQL, (menge, ID))
            conn.commit()
            return f"Bestand für ID {ID} erfolgreich um {menge} erhöht"
        except pyodbc.Error as e:
            return f"Fehler bei der Datenbankverbindung: {e}"
        finally:
            cursor.close()
            conn.close()
    
    def abbuchen(self, ID, menge):
        connectionString = f"""
        DRIVER={{ODBC Driver 18 for SQL Server}};
        SERVER={Lager.SERVER};
        DATABASE={Lager.DATABASE};
        Trusted_Connection=yes;
        TrustServerCertificate=yes;
        """
        try:
            conn = pyodbc.connect(connectionString)
            cursor = conn.cursor()
            print("Verbindung zum Lager hergestellt")

            SQL = f"""
            UPDATE [Beispiel-Firma].[dbo].[Materialien]
            SET Menge = Menge - ?
            WHERE ID = ?;
            """
            cursor.execute(SQL, (menge, ID))
            conn.commit()
            return f"Bestand für ID {ID} erfolgreich um {menge} verringert"
        except pyodbc.Error as e:
            return f"Fehler bei der Datenbankverbindung: {e}"
        finally:
            cursor.close()
            conn.close()
