-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema travelkeepdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema travelkeepdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `travelkeepdb` DEFAULT CHARACTER SET utf8 ;
USE `travelkeepdb` ;

-- -----------------------------------------------------
-- Table `travelkeepdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `share_w_friends` TINYINT(1) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`trips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`trips` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `rating` TINYINT(1) NULL,
  `start_location` VARCHAR(45) NULL,
  `end_location` VARCHAR(45) NULL,
  `trip_miles` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`photos_vids`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`photos_vids` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `photo` VARCHAR(100) NULL,
  `videos` VARCHAR(100) NULL,
  `trip_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_photos_vids_trips1_idx` (`trip_id` ASC),
  INDEX `fk_photos_vids_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_photos_vids_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_photos_vids_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `user_id` INT NOT NULL,
  `trip_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  INDEX `fk_comments_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`friends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friends_users_a_idx` (`user_id` ASC),
  INDEX `fk_friends_users_b_idx` (`friend_id` ASC),
  CONSTRAINT `fk_friends_users_a`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_friends_users1_b`
    FOREIGN KEY (`friend_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `trip_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `favorite_status` TINYINT(1) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users1_idx` (`user_id` ASC),
  INDEX `fk_favorites_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_favorites_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `trip_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `favorite_status` TINYINT(1) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users1_idx` (`user_id` ASC),
  INDEX `fk_favorites_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_favorites_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`participants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`participants` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `trip_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_participants_users1_idx` (`user_id` ASC),
  INDEX `fk_participants_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_participants_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_participants_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
