-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2022 at 07:40 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Id` int(11) NOT NULL,
  `BrandName` varchar(30) NOT NULL,
  `ProductName` varchar(30) NOT NULL,
  `EntryDate` date NOT NULL,
  `StockKg` int(11) NOT NULL,
  `PriceKg` varchar(30) NOT NULL,
  `Discount` int(45) NOT NULL,
  `FinalPrice` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`Id`, `BrandName`, `ProductName`, `EntryDate`, `StockKg`, `PriceKg`, `Discount`, `FinalPrice`) VALUES
(1, 'ITC', 'Rice', '2022-03-04', 125, '56', 0, '56'),
(2, 'ITC', 'wheat', '2022-11-10', 35, '35', 0, '35'),
(3, 'HUL', 'Besan ', '0000-00-00', 200, '65', 0, '65'),
(4, 'Ashirwad', 'wheat flour', '2022-11-10', 125, '80', 0, '80'),
(5, 'happy', 'waffers', '2022-11-04', 10, '25', 5, '20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
