-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: boots
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods` (
  `article` varchar(255) NOT NULL,
  `nameGood` varchar(255) DEFAULT NULL,
  `unit` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `idSupplier` int DEFAULT NULL,
  `idManufactor` int DEFAULT NULL,
  `category` enum('Женская обувь','Мужская обувь') DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `descript` text,
  `photoURL` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`article`),
  KEY `idSupplier` (`idSupplier`),
  KEY `idManufactor` (`idManufactor`),
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`idSupplier`) REFERENCES `suppliers` (`id`),
  CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`idManufactor`) REFERENCES `manufactor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES ('4CJUF','АМААМА','fsd',1000,1,1,'Женская обувь',15,2,'ВВВВВ','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('986NZ','dsa','s',1000,1,2,'Мужская обувь',10,4,'dfs','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('9E2ET','','31231',321312,1,1,'Мужская обувь',12,1,'','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('9ZU68','dasssda','fds',100,2,2,'Женская обувь',2,100,'fsf','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('B320R5','Туфли','шт.',4300,2,5,'Женская обувь',2,6,'Туфли Rieker женские демисезонные, размер 41, цвет коричневый','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/9.jpg'),('B431R5','Ботинки','шт.',2700,2,4,'Мужская обувь',2,5,'Мужские кожаные ботинки/мужские ботинки',NULL),('D268G5','Туфли','шт.',4399,2,4,'Женская обувь',3,12,'Туфли Rieker женские демисезонные, размер 36, цвет коричневый',NULL),('D329H3','Полуботинки','шт.',1890,2,5,'Женская обувь',4,4,'Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/8.jpg'),('D364R4','Туфли','шт.',12400,1,1,'Женская обувь',16,5,'Туфли Luiza Belly женские Kate-lazo черные из натуральной замши',NULL),('D572U8','Кроссовки','шт.',4100,2,3,'Мужская обувь',3,6,'129615-4 Кроссовки мужские','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/Снимок экрана 2024-02-28 023617.png'),('E482R4','Полуботинки','шт.',1800,1,1,'Женская обувь',2,14,'Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный',NULL),('F427R5','Ботинки','шт.',11800,2,4,'Женская обувь',15,11,'Ботинки на молнии с декоративной пряжкой FRAU',NULL),('F572H7','Туфли','шт.',2700,1,2,'Женская обувь',2,14,'Туфли Marco Tozzi женские летние, размер 39, цвет черный','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/7.jpg'),('F635R4','Ботинки','шт.',3244,2,2,'Женская обувь',2,13,'Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/2.jpg'),('G432E4','Туфли','шт.',2800,1,1,'Женская обувь',3,15,'Туфли kari женские TR-YR-413017, размер 37, цвет: черный','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/10.jpg'),('G531F4','Ботинки','шт.',6600,1,1,'Женская обувь',12,9,'Ботинки женские зимние ROMER арт. 893167-01 Черный',NULL),('G783F5','Ботинки','шт.',5900,1,4,'Мужская обувь',2,8,'Мужские ботинки Рос-Обувь кожаные с натуральным мехом','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/Снимок экрана 2026-02-16 145806.png'),('H535R5','Ботинки','шт.',2300,2,4,'Женская обувь',2,7,'Женские Ботинки демисезонные',NULL),('H782T5','Туфли','шт.',4499,1,1,'Мужская обувь',4,5,'Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/3.jpg'),('J384T6','Ботинки','шт.',3800,2,4,'Мужская обувь',2,16,'B3430/14 Полуботинки мужские Rieker','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/5.jpg'),('J542F5','Тапочки','шт.',500,1,1,'Мужская обувь',13,0,'Тапочки мужские Арт.70701-55-67син р.41',NULL),('K345R4','Полуботинки','шт.',2100,2,6,'Мужская обувь',2,3,'407700/01-02 Полуботинки мужские CROSBY',NULL),('K358H6','Тапочки','шт.',599,2,5,'Мужская обувь',20,2,'Тапочки мужские син р.41','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('L754R4','Полуботинки','шт.',1700,1,1,'Женская обувь',2,7,'Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный',NULL),('M542T5','Кроссовки','шт.',2800,2,4,'Мужская обувь',18,3,'Кроссовки мужские TOFA',NULL),('N457T5','s','сы',3500,1,1,'Женская обувь',15,1,'s','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/Снимок экрана 2024-02-26 173141.png'),('O754F4','Туфли','шт.',5400,2,4,'Женская обувь',4,18,'Туфли женские демисезонные Rieker артикул 55073-68/37',NULL),('S213E3','Полуботинки','шт.',2156,2,6,'Мужская обувь',3,6,'407700/01-01 Полуботинки мужские CROSBY',NULL),('S326R5','Тапочки','шт.',9900,2,6,'Мужская обувь',17,15,'Мужские кожаные тапочки \"Профиль С.Дали\"',NULL),('S634B5','Кеды','шт.',5500,2,6,'Мужская обувь',3,0,'Кеды Caprice мужские демисезонные, размер 42, цвет черный',NULL),('T324F5','Сапоги','шт.',4699,1,1,'Мужская обувь',2,5,'Сапоги замша Цвет: синий','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('XU7C2','','31231',321312,1,1,'Мужская обувь',12,1,'','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'),('А112Т4','Ботинки','шт.',4990,1,1,'Женская обувь',3,6,'Женские Ботинки демисезонные kari','C:/Users/Meow_Barsik/PycharmProjects/tovar/src/1.jpg');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufactor`
--

DROP TABLE IF EXISTS `manufactor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufactor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nameManufactor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufactor`
--

LOCK TABLES `manufactor` WRITE;
/*!40000 ALTER TABLE `manufactor` DISABLE KEYS */;
INSERT INTO `manufactor` VALUES (1,'Kari'),(2,'Marco Tozzi'),(3,'Poc'),(4,'Rieker'),(5,'Alessio Nesca'),(6,'CROSBY');
/*!40000 ALTER TABLE `manufactor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_compose`
--

DROP TABLE IF EXISTS `order_compose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_compose` (
  `idOrder` int NOT NULL,
  `idGood` varchar(255) NOT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`idOrder`,`idGood`),
  KEY `idGood` (`idGood`),
  CONSTRAINT `order_compose_ibfk_1` FOREIGN KEY (`idOrder`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_compose_ibfk_2` FOREIGN KEY (`idGood`) REFERENCES `goods` (`article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_compose`
--

LOCK TABLES `order_compose` WRITE;
/*!40000 ALTER TABLE `order_compose` DISABLE KEYS */;
INSERT INTO `order_compose` VALUES (3,'D572U8',10),(3,'J384T6',10),(4,'D329H3',4),(4,'F572H7',5),(5,'F635R4',2),(5,'А112Т4',2),(6,'G783F5',1),(6,'H782T5',1),(7,'D572U8',10),(7,'J384T6',10),(8,'D329H3',4),(8,'F572H7',5),(9,'B320R5',5),(9,'G432E4',1),(10,'E482R4',5),(10,'S213E3',5);
/*!40000 ALTER TABLE `order_compose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dateOrder` date DEFAULT NULL,
  `dateDelivery` date DEFAULT NULL,
  `idPoint` int DEFAULT NULL,
  `fio` varchar(255) DEFAULT NULL,
  `getCode` int DEFAULT NULL,
  `orderStatus` enum('Доставлено','Недоставлено') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idPoint` (`idPoint`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`idPoint`) REFERENCES `pickup_points` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (3,'2025-03-21','2025-04-22',2,'Сазонов Руслан Германович',903,'Доставлено'),(4,'2025-02-20','2025-04-23',11,'Одинцов Серафим Артёмович',904,'Доставлено'),(5,'2025-03-17','2025-04-24',2,'Степанов Михаил Артёмович',905,'Доставлено'),(6,'2025-03-01','2025-04-25',15,'Никифорова Весения Николаевна',906,'Доставлено'),(7,'2025-02-28','2025-04-26',3,'Сазонов Руслан Германович',907,'Доставлено'),(8,'2025-03-31','2025-04-27',19,'Одинцов Серафим Артёмович',908,'Недоставлено'),(9,'2025-04-02','2025-04-28',5,'Степанов Михаил Артёмович',909,'Недоставлено'),(10,'2025-04-03','2025-04-29',19,'Степанов Михаил Артёмович',910,'Недоставлено');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pickup_points`
--

DROP TABLE IF EXISTS `pickup_points`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pickup_points` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pickup_points`
--

LOCK TABLES `pickup_points` WRITE;
/*!40000 ALTER TABLE `pickup_points` DISABLE KEYS */;
INSERT INTO `pickup_points` VALUES (1,'fsadfsadf, 32'),(2,'125061, г. Лесной, ул. Подгорная, 8'),(3,'630370, г. Лесной, ул. Шоссейная, 24'),(4,'400562, г. Лесной, ул. Зеленая, 32'),(5,'614510, г. Лесной, ул. Маяковского, 47'),(6,'410542, г. Лесной, ул. Светлая, 46'),(7,'620839, г. Лесной, ул. Цветочная, 8'),(8,'443890, г. Лесной, ул. Коммунистическая, 1'),(9,'603379, г. Лесной, ул. Спортивная, 46'),(10,'603721, г. Лесной, ул. Гоголя, 41'),(11,'125061, г. Лесной, ул. Подгорная, 8'),(12,'614611, г. Лесной, ул. Молодежная, 50'),(13,'454311, г.Лесной, ул. Новая, 19'),(14,'660007, г.Лесной, ул. Октябрьская, 19'),(15,'603036, г. Лесной, ул. Садовая, 4'),(16,'394060, г.Лесной, ул. Фрунзе, 43'),(17,'410661, г. Лесной, ул. Школьная, 50'),(18,'625590, г. Лесной, ул. Коммунистическая, 20'),(19,'625683, г. Лесной, ул. 8 Марта'),(20,'450983, г.Лесной, ул. Комсомольская, 26'),(21,'394782, г. Лесной, ул. Чехова, 3'),(22,'603002, г. Лесной, ул. Дзержинского, 28'),(23,'450558, г. Лесной, ул. Набережная, 30'),(24,'344288, г. Лесной, ул. Чехова, 1'),(25,'614164, г.Лесной, ул. Степная, 30'),(26,'394242, г. Лесной, ул. Коммунистическая, 43'),(27,'660540, г. Лесной, ул. Солнечная, 25'),(28,'125837, г. Лесной, ул. Шоссейная, 40'),(29,'125703, г. Лесной, ул. Партизанская, 49'),(30,'625283, г. Лесной, ул. Победы, 46'),(31,'614753, г. Лесной, ул. Полевая, 35'),(32,'426030, г. Лесной, ул. Маяковского, 44'),(33,'450375, г. Лесной ул. Клубная, 44'),(34,'625560, г. Лесной, ул. Некрасова, 12'),(35,'630201, г. Лесной, ул. Комсомольская, 17'),(36,'190949, г. Лесной, ул. Мичурина, 26'),(37,'fdsafds'),(38,'fasdf'),(39,''),(40,''),(41,'fsdfsf'),(42,'fsdfafdsf');
/*!40000 ALTER TABLE `pickup_points` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nameSupplier` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Kari'),(2,'Обувь для вас');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idRole` int DEFAULT NULL,
  `secondName` varchar(255) DEFAULT NULL,
  `firstName` varchar(255) DEFAULT NULL,
  `patronymic` varchar(255) DEFAULT NULL,
  `login` varchar(255) DEFAULT NULL,
  `passwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idRole` (`idRole`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`idRole`) REFERENCES `usertypes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,1,'Никифорова','Весения','Николаевна','94d5ous@gmail.com','uzWC67'),(2,1,'Сазонов','Руслан','Германович','uth4iz@mail.com','2L6KZG'),(3,1,'Одинцов','Серафим','Артёмович','yzls62@outlook.com','JlFRCZ'),(4,2,'Степанов','Михаил','Артёмович','1diph5e@tutanota.com','8ntwUp'),(5,2,'Ворсин','Петр','Евгеньевич','tjde7c@yahoo.com','YOyhfR'),(6,2,'Старикова','Елена','Павловна','wpmrc3do@tutanota.com','RSbvHv'),(7,3,'Михайлюк','Анна','Вячеславовна','5d4zbu@tutanota.com','rwVDh9'),(8,3,'Ситдикова','Елена','Анатольевна','ptec8ym@yahoo.com','LdNyos'),(9,3,'Ворсин','Петр','Евгеньевич','1qz4kw@mail.com','gynQMT'),(10,3,'Старикова','Елена','Павловна','4np6se@mail.com','AtnDjr');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usertypes`
--

DROP TABLE IF EXISTS `usertypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usertypes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nameRole` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usertypes`
--

LOCK TABLES `usertypes` WRITE;
/*!40000 ALTER TABLE `usertypes` DISABLE KEYS */;
INSERT INTO `usertypes` VALUES (1,'Администратор'),(2,'Менеджер'),(3,'Авторизированный клиент');
/*!40000 ALTER TABLE `usertypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-01 19:27:41
