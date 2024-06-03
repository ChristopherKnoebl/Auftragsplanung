
CREATE TABLE Materialien(ID  INT PRIMARY KEY,Bezeichnung TEXT);
INSERT INTO Materialien Values (1, 'Holz_1');
INSERT INTO Materialien Values (2, 'Holz_2');
INSERT INTO Materialien Values (3, 'Schrauben');
INSERT INTO Materialien Values (4, 'Leim');
INSERT INTO Materialien Values (5, 'Scharniere');
go

CREATE TABLE Produkte(ID  INTEGER PRIMARY KEY,Bezeichnung TEXT);
INSERT INTO Produkte Values (1, 'Tisch_1');
INSERT INTO Produkte Values (2, 'Tisch_2');
INSERT INTO Produkte Values (3, 'Stuhl_1');
INSERT INTO Produkte Values (4, 'Stuhl_2');
INSERT INTO Produkte Values (5, 'Schrank_1');
go

CREATE TABLE Produkt_Material_Verbund(ID  INTEGER PRIMARY KEY, ProduktID INT, MaterialID INT, Menge INT,
FOREIGN KEY (ProduktID) REFERENCES Produkt(ID), FOREIGN KEY (MaterialID) REFERENCES Material(ID));
INSERT INTO Produkt_Material_Verbund Values (1, 1, 1, 5);
INSERT INTO Produkt_Material_Verbund Values (2, 1, 3, 15);
INSERT INTO Produkt_Material_Verbund Values (3, 1, 4, 0.5);
INSERT INTO Produkt_Material_Verbund Values (4, 2, 2, 7);
INSERT INTO Produkt_Material_Verbund Values (5, 2, 3, 15);
INSERT INTO Produkt_Material_Verbund Values (6, 2, 4, 0.5);
INSERT INTO Produkt_Material_Verbund Values (7, 3, 1, 3);
INSERT INTO Produkt_Material_Verbund Values (8, 3, 3, 25);
INSERT INTO Produkt_Material_Verbund Values (9, 3, 4, 0.5);
INSERT INTO Produkt_Material_Verbund Values (10, 4, 2, 3);
INSERT INTO Produkt_Material_Verbund Values (11, 4, 3, 25);
INSERT INTO Produkt_Material_Verbund Values (12, 4, 4, 0.25);
INSERT INTO Produkt_Material_Verbund Values (13, 5, 1, 5);
INSERT INTO Produkt_Material_Verbund Values (14, 5, 2, 4);
INSERT INTO Produkt_Material_Verbund Values (15, 5, 3, 15);
INSERT INTO Produkt_Material_Verbund Values (16, 5, 4, 0.5);
INSERT INTO Produkt_Material_Verbund Values (17, 5, 5, 8);
go


CREATE TABLE Lager( ID  INTEGER PRIMARY KEY, Bezeichnung TEXT);
INSERT INTO Lager Values (1, 'Hauptlager');
INSERT INTO Lager Values (2, 'Fertigungslager');
go

CREATE TABLE Lagerbestand( ID INTEGER PRIMARY KEY, LagerID INT , MaterialID INT , Menge INT,
FOREIGN KEY (LagerID) REFERENCES Lager(ID), FOREIGN KEY (MaterialID) REFERENCES Material(ID));
INSERT INTO Lagerbestand Values (1, 1, 1, 100);
INSERT INTO Lagerbestand Values (2, 1, 2, 200);
INSERT INTO Lagerbestand Values (3, 1, 3, 500);
INSERT INTO Lagerbestand Values (4, 1, 4, 300);
INSERT INTO Lagerbestand Values (5, 1, 5, 0);
INSERT INTO Lagerbestand Values (6,2, 1, 50);
INSERT INTO Lagerbestand Values (7,2, 2, 100);
INSERT INTO Lagerbestand Values (8,2, 3, 250);
INSERT INTO Lagerbestand Values (9,2, 4, 150);
INSERT INTO Lagerbestand Values (10,2, 5, 150);
go

CREATE TABLE Status( ID INTEGER PRIMARY KEY, Status TEXT);
INSERT INTO Status Values (1, 'Material fehlt, Disponent informiert');
INSERT INTO Status Values (2, 'Material fehlt, aus Hauptlager angefordert');
INSERT INTO Status Values (3, 'Auftrag kommissioniert');
INSERT INTO Status Values (4, 'Auftrag in Produktion');
INSERT INTO Status Values (5, 'Auftrag abgeschlossen');
go
