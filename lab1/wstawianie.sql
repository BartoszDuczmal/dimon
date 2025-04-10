USE dbSPJ;

SET foreign_key_checks = 0;

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/bron.cvg'
INTO TABLE bron
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/mysliwi.cvg'
INTO TABLE mysliwi
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/mysliwi_bron.cvg'
INTO TABLE mysliwi_bron
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/obwody.cvg'
INTO TABLE obwody
FIELDS TERMINATED BY ', '
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/sektory.cvg'
INTO TABLE sektory
FIELDS TERMINATED BY ', '
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/pozwolenia.cvg'
INTO TABLE pozwolenia
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/Users/Bartosz/Desktop/pl/data/straznicy.cvg'
INTO TABLE straznicy
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

SET foreign_key_checks = 1;