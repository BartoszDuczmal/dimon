import os
from faker import Faker
from random import choice

# --------------------------
# KONFIGURACJA GŁÓWNA
# --------------------------

# Stałe konfiguracyjne
MAX_AMOUNT = 1000          # Maksymalna liczba myśliwych
NUM_SECTORS = 100          # Liczba sektorów łowieckich
SQUARE = []                # Lista przechowująca powierzchnie obwodów łowieckich
MAX_NUM_SECTORS = []       # Lista przechowująca maksymalną liczbę sektorów dla każdego obwodu
HUNTSMEN_SECTORS = [i+1 for i in range(NUM_SECTORS)]  # Lista dostępnych sektorów dla strażników
HUNTERS = []               # Lista przechowująca numery legitymacji myśliwskich

# Ścieżki do plików
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Katalog skryptu
DATA_DIR = os.path.join(SCRIPT_DIR, 'data')              # Katalog na wygenerowane dane

# Inicjalizacja generatora danych testowych Faker dla lokalizacji polskiej
fake_pl = Faker('pl_PL')

# --------------------------
# DANE DO GENERACJI
# --------------------------

# Dane możliwe do wygenerowania
sex = ['m', 'k']  # Płeć: m - mężczyzna, k - kobieta
price = [i for i in range(300, 1000, 150)]  # Możliwe ceny pozwoleń

# Lista zwierząt łownych
animals = ['kaczka', 'gęś', 'cietrzew', 'zając szarak', 'lis',
           'bóbr', 'wydra', 'sarna', 'łoś', 'jarząbek',
           'jeleń', 'bekas', 'niedźwiedź', 'wilk', 'dzik',
           'głuszec', 'przepiórka', 'kuropatwa', 'zając bielak', 'borsuk',
           'kuna', 'norka', 'słonka', 'kuropatwa', 'przepiórka',
           'krzyżówka', 'czernica', 'cyraneczka', 'piżmak', 'tchórz']

# Typy broni
type_1 = "gładkolufowa"
type_2 = "gwintowana"
type_3 = "kombinowana"

# Lista dostępnej broni myśliwskiej
weapon = [{'brand': 'Mossberg 500', 'type': type_1, 'num_barrels': 1, 'caliber': 12},
          {'brand': 'Remington 870', 'type': type_1, 'num_barrels': 1, 'caliber': 16},
          # ... (pozostałe elementy listy broni)
          {'brand': 'Merkel RX Helix', 'type': type_3, 'num_barrels': 2, 'caliber': '7.62 mm'}]

# --------------------------
# FUNKCJE GENERUJĄCE DANE
# --------------------------

def create_data_directory():
    """
    Tworzy katalog na dane jeśli nie istnieje.
    
    Returns:
        bool: True jeśli katalog został utworzony lub już istnieje, False w przypadku błędu
    """
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        print(f"[INFO] Utworzono katalog danych: {DATA_DIR}")
        return True
    except Exception as e:
        print(f"[ERROR] Nie można utworzyć katalogu: {e}")
        return False

def check_permissions():
    """
    Sprawdza uprawnienia do zapisu w katalogu danych.
    
    Returns:
        bool: True jeśli uprawnienia są wystarczające, False w przeciwnym przypadku
    """
    test_file = os.path.join(DATA_DIR, 'test_permission.txt')
    try:
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"[ERROR] Brak uprawnień do zapisu: {e}")
        return False

def generate_hunting_grounds():
    """
    Generuje dane o obwodach łowieckich i zapisuje je do pliku 'obwody.cvg'.
    
    Format pliku:
        nazwa_obwodu, powierzchnia, maksymalna_liczba_sektorów
    """
    file_path = os.path.join(DATA_DIR, 'obwody.cvg')
    
    # Lista polskich województw
    voivodeships = [
        "Dolnośląskie", "Kujawsko-Pomorskie", "Lubelskie", "Lubuskie",
        "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie",
        "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie",
        "Świętokrzyskie", "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"
    ]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        temp = []
        i = 0

        while i < 70:
            # Generowanie unikalnej nazwy obwodu łowieckiego
            base_name = choice(voivodeships)
            name = f"{base_name} {fake_pl.unique.random_number(digits=2)}"
            
            if name not in temp:
                temp.append(name)
            else:
                continue

            s = choice(range(100, 10000))  # Losowa powierzchnia obwodu
            SQUARE.append(s)
            max_num = choice(range(1, 10))  # Maksymalna liczba sektorów
            MAX_NUM_SECTORS.append(max_num)

            line = "{0}, {1}, {2}\n".format(
                name,
                s,
                max_num
            )

            f.write(line)
            i += 1
        print(f"[INFO] Utworzono plik: {file_path}")

def generate_sectors():
    """
    Generuje dane o sektorach łowieckich i zapisuje je do pliku 'sektory.cvg'.
    
    Format pliku:
        powierzchnia, id_obwodu
    """
    file_path = os.path.join(DATA_DIR, 'sektory.cvg')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        i = 1
        while i <= NUM_SECTORS:
            id_husbandry = choice(range(1, 71))
            if MAX_NUM_SECTORS[id_husbandry - 1] == 0:
                continue

            s = choice(range(100, 10000))  # Losowa powierzchnia sektora
            if SQUARE[id_husbandry - 1] < s:
                continue
            if SQUARE[id_husbandry - 1] == s:
                if MAX_NUM_SECTORS[id_husbandry - 1] == 1:
                    MAX_NUM_SECTORS[id_husbandry - 1] -= 1
                    SQUARE[id_husbandry - 1] -= s
                    i += 1
                else:
                    continue
            else:
                if MAX_NUM_SECTORS[id_husbandry - 1]:
                    MAX_NUM_SECTORS[id_husbandry - 1] -= 1
                    SQUARE[id_husbandry - 1] -= s
                    i += 1

            line = "{0}, {1}\n".format(
                s,
                id_husbandry
            )

            f.write(line)
        print(f"[INFO] Utworzono plik: {file_path}")

def generate_hunters():
    """
    Generuje dane o myśliwych i zapisuje je do pliku 'mysliwi.cvg'.
    
    Format pliku:
        numer_legitymacji|nazwisko|imię|data_urodzenia|płeć|numer_licencji|adres|telefon|email
    """
    file_path = os.path.join(DATA_DIR, 'mysliwi.cvg')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        for i in range(MAX_AMOUNT):
            sex_p = choice(sex)
            if sex_p == 'm':
                surname = fake_pl.last_name_male()
                name = fake_pl.first_name_male()
            else:
                surname = fake_pl.last_name_female()
                name = fake_pl.first_name_female()

            date_of_brth = fake_pl.date_of_birth(None, 21, 80)
            address = fake_pl.address().replace('\n', ' ')
            phone = fake_pl.phone_number()
            email = fake_pl.email()
            num_license = fake_pl.license_plate()
            num_ticket = fake_pl.ean(length=8)

            HUNTERS.append(num_ticket)

            line = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}\n".format(
                num_ticket,
                surname,
                name,
                date_of_brth,
                sex_p,
                num_license,
                address,
                phone,
                email
            )

            f.write(line)
        print(f"[INFO] Utworzono plik: {file_path}")

def generate_huntsmen():
    """
    Generuje dane o strażnikach łowieckich i zapisuje je do pliku 'straznicy.cvg'.
    
    Format pliku:
        id_sektora,nazwisko,imię,data_urodzenia,płeć,doświadczenie,telefon,email,pensja
    """
    file_path = os.path.join(DATA_DIR, 'straznicy.cvg')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        i = 0
        while i < NUM_SECTORS:
            ind = choice(range(len(HUNTSMEN_SECTORS)))
            id_sector = HUNTSMEN_SECTORS[ind]
            del HUNTSMEN_SECTORS[ind]

            sex_p = choice(sex)
            if sex_p == 'm':
                surname = fake_pl.last_name_male()
                name = fake_pl.first_name_male()
            else:
                surname = fake_pl.last_name_female()
                name = fake_pl.first_name_female()

            date_of_brth = fake_pl.date_of_birth(None, 21, 80)
            experience = choice(range(0, 50))
            phone = fake_pl.phone_number()
            email = fake_pl.email()
            salary = choice(range(4000, 15000, 500))

            line = "{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(
                id_sector,
                surname,
                name,
                date_of_brth,
                sex_p,
                experience,
                phone,
                email,
                salary
            )

            f.write(line)
            i += 1
        print(f"[INFO] Utworzono plik: {file_path}")

def generate_voucher():
    """
    Generuje dane o pozwoleniach na polowanie i zapisuje je do pliku 'pozwolenia.cvg'.
    
    Format pliku:
        zwierze,czas_trwania,ilość,cena,id_sektora,id_myśliwego
    """
    file_path = os.path.join(DATA_DIR, 'pozwolenia.cvg')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        for i in range(MAX_AMOUNT + 200):
            animal = choice(animals)
            duration = choice(range(1, 100))
            amount = choice(range(1, 10))
            prc = choice(price) * amount
            id_sector = choice(range(1, NUM_SECTORS))
            ind = choice(range(1, MAX_AMOUNT))
            id_hunter = HUNTERS[ind]

            line = "{0},{1},{2},{3},{4},{5}\n".format(
                animal,
                duration,
                amount,
                prc,
                id_sector,
                id_hunter
            )

            f.write(line)
        print(f"[INFO] Utworzono plik: {file_path}")

def generate_weapon():
    """
    Generuje dane o broni myśliwskiej i zapisuje je do pliku 'bron.cvg'.
    
    Format pliku:
        marka,typ,liczba_luf,kaliber
    """
    file_path = os.path.join(DATA_DIR, 'bron.cvg')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        for i in range(MAX_AMOUNT + 200):
            ind = choice(range(0, len(weapon)))

            brand = weapon[ind]['brand']
            type_w = weapon[ind]['type']
            num_barrels = weapon[ind]['num_barrels']
            caliber = weapon[ind]['caliber']

            line = "{0},{1},{2},{3}\n".format(
                brand,
                type_w,
                num_barrels,
                caliber
            )

            f.write(line)
        print(f"[INFO] Utworzono plik: {file_path}")

def generate_hunter_weapon():
    """
    Generuje powiązania między myśliwymi a bronią i zapisuje je do pliku 'mysliwi_bron.cvg'.
    
    Format pliku:
        id_myśliwego,id_broni
    """
    file_path = os.path.join(DATA_DIR, 'mysliwi_bron.cvg')
    
    # Wczytanie istniejących myśliwych
    hunters = []
    hunters_file = os.path.join(DATA_DIR, 'mysliwi.cvg')
    try:
        with open(hunters_file, 'r', encoding='utf-8') as file_hunters:
            for row in file_hunters.readlines():
                hunters.append(row.split('|')[0])
    except FileNotFoundError:
        print(f"[ERROR] Nie znaleziono pliku: {hunters_file}")
        return

    with open(file_path, 'w', encoding='utf-8') as f:
        for i in range(MAX_AMOUNT):
            ind_hunter = choice(hunters)
            ind_weapon = choice(range(1, MAX_AMOUNT + 200))

            line = "{0},{1}\n".format(
                ind_hunter,
                ind_weapon
            )

            f.write(line)
        print(f"[INFO] Utworzono plik: {file_path}")

# --------------------------
# GŁÓWNA CZĘŚĆ PROGRAMU
# --------------------------

if __name__ == "__main__":
    print("="*50)
    print("Rozpoczęcie generowania danych")
    print(f"Katalog roboczy: {SCRIPT_DIR}")
    print(f"Katalog danych: {DATA_DIR}")
    print("="*50)
    
    # Sprawdzenie i utworzenie katalogu danych
    if not create_data_directory():
        exit(1)
        
    # Sprawdzenie uprawnień do zapisu
    if not check_permissions():
        exit(1)
    
    # Generowanie danych w odpowiedniej kolejności
    generate_hunting_grounds()    # 1. Generowanie obwodów łowieckich
    generate_sectors()           # 2. Generowanie sektorów
    generate_hunters()           # 3. Generowanie myśliwych
    generate_huntsmen()          # 4. Generowanie strażników
    generate_voucher()           # 5. Generowanie pozwoleń
    generate_weapon()            # 6. Generowanie broni
    generate_hunter_weapon()     # 7. Generowanie powiązań myśliwi-broń
    
    print("="*50)
    print("Generowanie danych zakończone pomyślnie!")
    print(f"Wszystkie pliki zapisano w: {DATA_DIR}")
    print("="*50)