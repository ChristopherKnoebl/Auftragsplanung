import sqlite3
 


connection_obj = sqlite3.connect('testfirma.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS Materialien")
sql = """ CREATE TABLE IF NOT EXISTS Materialien (
            Name VARCHAR(255) NOT NULL,
            Bestand INT
        )"""
cursor_obj.execute(sql)

sql = """
            INSERT OR REPLACE INTO Materialien Values ("Holz", 10);
            INSERT OR REPLACE INTO Materialien Values ("Eisen", 5);
            INSERT OR REPLACE INTO Materialien Values ("Schrauben", 50);
            INSERT OR REPLACE INTO Materialien Values ("Nägel", 100)
        """
 
cursor_obj.executescript(sql)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()