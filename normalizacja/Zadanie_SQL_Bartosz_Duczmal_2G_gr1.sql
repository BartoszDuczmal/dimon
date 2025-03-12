-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 04, 2025 at 06:47 PM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zadanie_sql`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `odbiorcy`
--

CREATE TABLE `odbiorcy` (
  `nrOdbiorcy` int(5) NOT NULL,
  `nazwaOdbiorcy` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `odbiorcy`
--

INSERT INTO `odbiorcy` (`nrOdbiorcy`, `nazwaOdbiorcy`) VALUES
(3335, 'Nowak'),
(3337, 'Malinowski'),
(4444, 'Kowalski');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `produkty`
--

CREATE TABLE `produkty` (
  `nrProduktu` int(5) NOT NULL,
  `nazwaProduktu` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produkty`
--

INSERT INTO `produkty` (`nrProduktu`, `nazwaProduktu`) VALUES
(340, 'Zaprawa (1kg)'),
(342, 'Cement (1kg)'),
(487, 'dachówki (niebieskie)'),
(488, 'dachówki (białe)'),
(489, 'dachówki (czerwone)');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zamowienia`
--

CREATE TABLE `zamowienia` (
  `id` int(5) NOT NULL,
  `nrZamowienia` text NOT NULL,
  `dataZamowienia` date NOT NULL,
  `nrOdbiorcy` int(5) NOT NULL,
  `nrProduktu` int(5) NOT NULL,
  `ilosc` int(4) NOT NULL,
  `cenaJednostkowa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `zamowienia`
--

INSERT INTO `zamowienia` (`id`, `nrZamowienia`, `dataZamowienia`, `nrOdbiorcy`, `nrProduktu`, `ilosc`, `cenaJednostkowa`) VALUES
(1, '0/733', '2012-02-01', 3335, 487, 200, 45689),
(2, '0/734', '2012-02-08', 4444, 488, 300, 43862),
(3, '0/775', '2012-02-10', 4444, 489, 150, 45689),
(4, '0/775', '2012-02-01', 3335, 340, 10, 45789),
(5, '0/734', '2012-02-08', 4444, 340, 30, 45789),
(6, '0/734', '2012-02-08', 4444, 342, 30, 15),
(7, '0/736', '2012-02-01', 3337, 488, 400, 43862);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `odbiorcy`
--
ALTER TABLE `odbiorcy`
  ADD PRIMARY KEY (`nrOdbiorcy`);

--
-- Indeksy dla tabeli `produkty`
--
ALTER TABLE `produkty`
  ADD PRIMARY KEY (`nrProduktu`);

--
-- Indeksy dla tabeli `zamowienia`
--
ALTER TABLE `zamowienia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nrOdbiorcy` (`nrOdbiorcy`),
  ADD KEY `nrProduktu` (`nrProduktu`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `odbiorcy`
--
ALTER TABLE `odbiorcy`
  MODIFY `nrOdbiorcy` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4445;

--
-- AUTO_INCREMENT for table `produkty`
--
ALTER TABLE `produkty`
  MODIFY `nrProduktu` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=490;

--
-- AUTO_INCREMENT for table `zamowienia`
--
ALTER TABLE `zamowienia`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `zamowienia`
--
ALTER TABLE `zamowienia`
  ADD CONSTRAINT `zamowienia_ibfk_1` FOREIGN KEY (`nrOdbiorcy`) REFERENCES `odbiorcy` (`nrOdbiorcy`),
  ADD CONSTRAINT `zamowienia_ibfk_2` FOREIGN KEY (`nrProduktu`) REFERENCES `produkty` (`nrProduktu`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
