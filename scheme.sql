DROP DATABASE IF EXISTS `dg`;
CREATE DATABASE `dg` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `dg`;
SET NAMES utf8;
SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

# dg user表
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nickname` VARCHAR(128) NOT NULL,
	  `wechat` VARCHAR(128),
    `qq` VARCHAR(128),
    `email` VARCHAR(128),
    `avatar` VARCHAR(128),
	  `created_at` DATETIME NOT NULL,
    `shopname` VARCHAR(128) NOT NULL,
    `shopdesp` VARCHAR(256),
    `shopother` VARCHAR(256),
    `status` VARCHAR(32),
    `updated_at` DATETIME,
	  KEY (`created_at`),
    KEY (`status`),
    KEY (`updated_at`),
    KEY (`shopname`),
    KEY (`nickname`)
)DEFAULT CHARSET = UTF8;


# dg goods表
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `goodsname` VARCHAR(128) NOT NULL,
	  `price` VARCHAR(32),
    `hot` int DEFAULT 0,
    `goodsdesp` VARCHAR(128),
	  `created_at` DATETIME NOT NULL,
    `owner` int NOT NULL,
    `picurls` VARCHAR(256),
    `content` VARCHAR(256),
    `status` VARCHAR(32),
    `updated_at` DATETIME,
	  KEY (`created_at`),
    KEY (`status`),
    KEY (`updated_at`),
    KEY (`owner`),
    KEY (`goodsname`)
)DEFAULT CHARSET = UTF8;