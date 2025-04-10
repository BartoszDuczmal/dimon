DROP DATABASE IF EXISTS dbSPJ;
CREATE DATABASE dbSPJ;
USE dbSPJ;

-- Tabela: bron
CREATE TABLE bron (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(100),
    typ VARCHAR(50),
    liczba_luf INT,
    kaliber VARCHAR(20)
);

-- Tabela: mysliwi
CREATE TABLE mysliwi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    adres VARCHAR(100),
    telefon VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela: mysliwi_bron
CREATE TABLE mysliwi_bron (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_mysliwego INT,
    adres_zameldowania VARCHAR(100),
    adres_zamieszkania VARCHAR(100),
    id_broni INT,
    FOREIGN KEY (id_mysliwego) REFERENCES mysliwi(id),
    FOREIGN KEY (id_broni) REFERENCES bron(id)
);

-- Tabela: obwody
CREATE TABLE obwody (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(100),
    powierzchnia_km2 DECIMAL(8,2),
    liczba_sektorow INT
);

-- Tabela: pozwolenia
CREATE TABLE pozwolenia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gatunek VARCHAR(100),
    id_mysliwego INT,
    id_obwodu INT,
    czas_trwania_dni INT,
    liczba_sztuk INT,
    numer_pozwolenia VARCHAR(20),
    FOREIGN KEY (id_mysliwego) REFERENCES mysliwi(id),
    FOREIGN KEY (id_obwodu) REFERENCES obwody(id)
);

-- Tabela: sektory
CREATE TABLE sektory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numer_sektora INT,
    id_obwodu INT,
    FOREIGN KEY (id_obwodu) REFERENCES obwody(id)
);

-- Tabela: straznicy
CREATE TABLE straznicy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numer_legitymacji VARCHAR(20),
    nazwisko VARCHAR(50),
    imie VARCHAR(50),
    data_urodzenia DATE,
    plec CHAR(1),
    id_sektora INT,
    telefon VARCHAR(20),
    email VARCHAR(100),
    pensja DECIMAL(10,2),
    FOREIGN KEY (id_sektora) REFERENCES sektory(id)
);

-- Ładowanie danych
LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/bron.cvg'
INTO TABLE bron
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/mysliwi.cvg'
INTO TABLE mysliwi
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/mysliwi-bron.cvg'
INTO TABLE mysliwi_bron
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/obwody.cvg'
INTO TABLE obwody
FIELDS TERMINATED BY ', '
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/pozwolenia.cvg'
INTO TABLE pozwolenia
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/sektory.cvg'
INTO TABLE sektory
FIELDS TERMINATED BY ', '
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/Users/Bartosz/Desktop/pl/data/straznicy.cvg'
INTO TABLE straznicy
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
