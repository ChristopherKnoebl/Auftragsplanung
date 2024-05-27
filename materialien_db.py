import sqlite3

# erstelle und befülle die Materialien-Tabelle
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql_script = """
CREATE TABLE Materialien(ID  INT PRIMARY KEY,Bezeichnung TEXT);
INSERT OR REPLACE INTO Materialien Values (1, 'Holz_1');
INSERT OR REPLACE INTO Materialien Values (2, 'Holz_2');
INSERT OR REPLACE INTO Materialien Values (3, 'Schrauben');
INSERT OR REPLACE INTO Materialien Values (4, 'Leim');
INSERT OR REPLACE INTO Materialien Values (5, 'Scharniere')
"""
cursor.executescript(sql_script)
connection.commit()

# erstelle und befülle die Produkt-Tabelle
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql_script = """
CREATE TABLE Produkte(ID  INTEGER PRIMARY KEY,Bezeichnung TEXT);
INSERT OR REPLACE INTO Produkte Values (1, 'Tisch_1');
INSERT OR REPLACE INTO Produkte Values (2, 'Tisch_2');
INSERT OR REPLACE INTO Produkte Values (3, 'Stuhl_1');
INSERT OR REPLACE INTO Produkte Values (4, 'Stuhl_2');
INSERT OR REPLACE INTO Produkte Values (5, 'Schrank_1');
"""
cursor.executescript(sql_script)
connection.commit()

# erstelle und befülle die Produkt-Material-Verknüfungs-Tabelle
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql_script = """
CREATE TABLE Produkt_Material_Verbund(ID  INTEGER PRIMARY KEY, ProduktID INT, MaterialID INT, Menge INT,
FOREIGN KEY (ProduktID) REFERENCES Produkt(ID), FOREIGN KEY (MaterialID) REFERENCES Material(ID));
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (1, 1, 1);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (2, 1, 3);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (3, 1, 4);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (4, 2, 2);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (5, 2, 3);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (6, 2, 4);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (7, 3, 1);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (8, 3, 3);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (9, 3, 4);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (10, 4, 2);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (11, 4, 3);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (12, 4, 4);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (13, 5, 1);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (14, 5, 2);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (15, 5, 3);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (16, 5, 4);
INSERT OR REPLACE INTO Produkt_Material_Verbund Values (17, 5, 5);
"""
cursor.executescript(sql_script)
connection.commit()

# erstelle und befülle die Lager-Tabelle
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql_script = """
CREATE TABLE Lager( ID  INTEGER PRIMARY KEY, Bezeichnung TEXT);
INSERT OR REPLACE INTO Lager Values (1, 'Hauptlager');
INSERT OR REPLACE INTO Lager Values (2, 'Fertigungslager');
"""
cursor.executescript(sql_script)
connection.commit()

# erstelle und befülle die Lagerbestands-Tabelle
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql_script = """
CREATE TABLE Lagerbestand( ID INTEGER PRIMARY KEY, LagerID INT , MaterialID INT , Menge INT,
FOREIGN KEY (LagerID) REFERENCES Lager(ID), FOREIGN KEY (MaterialID) REFERENCES Material(ID));
INSERT OR REPLACE INTO Lagerbestand Values (1, 1, 1, 100);
INSERT OR REPLACE INTO Lagerbestand Values (2, 1, 2, 200);
INSERT OR REPLACE INTO Lagerbestand Values (3, 1, 3, 500);
INSERT OR REPLACE INTO Lagerbestand Values (4, 1, 4, 300);
INSERT OR REPLACE INTO Lagerbestand Values (5, 1, 5, 0);
INSERT OR REPLACE INTO Lagerbestand Values (6,2, 1, 50);
INSERT OR REPLACE INTO Lagerbestand Values (7,2, 2, 100);
INSERT OR REPLACE INTO Lagerbestand Values (8,2, 3, 250);
INSERT OR REPLACE INTO Lagerbestand Values (9,2, 4, 150);
INSERT OR REPLACE INTO Lagerbestand Values (10,2, 5, 150);
"""
cursor.executescript(sql_script)
connection.commit()

# erstelle und befülle die Auftragsstatus-Tabelle
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()
sql_script = """
"CREATE TABLE Status( ID INTEGER PRIMARY KEY, Status TEXT);
INSERT OR REPLACE INTO Status Values (1, 'Material fehlt, Disponent informiert');
INSERT OR REPLACE INTO Status Values (2, 'Material fehlt, aus Hauptlager angefordert');
INSERT OR REPLACE INTO Status Values (3, 'Auftrag kommissioniert');
INSERT OR REPLACE INTO Status Values (4, 'Auftrag in Produktion');
INSERT OR REPLACE INTO Status Values (5, 'Auftrag abgeschlossen');
"""
cursor.executescript(sql_script)
connection.commit()