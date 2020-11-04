-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_teamproject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_teamproject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_teamproject` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `db_teamproject` ;

-- -----------------------------------------------------
-- Table `db_teamproject`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`student` (
  `student_id` VARCHAR(12) NOT NULL,
  `password` VARCHAR(15) NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `major` VARCHAR(12) NULL,
  `register` VARCHAR(5) NULL,
  `division` VARCHAR(5) NULL,
  `phone_number` VARCHAR(20) NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE INDEX `student_id_UNIQUE` (`student_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `db_teamproject`.`subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`subject` (
  `subject_id` VARCHAR(20) NOT NULL,
  `term` VARCHAR(10) NOT NULL,
  `subject_name` VARCHAR(50) NOT NULL,
  `division` VARCHAR(10) NULL DEFAULT NULL,
  `is_major` TINYINT NOT NULL,
  `class_hours` INT NOT NULL,
  `professor_name` VARCHAR(20) NULL DEFAULT NULL,
  `day1` VARCHAR(10) NULL DEFAULT NULL,
  `time1` VARCHAR(10) NULL DEFAULT NULL,
  `day2` VARCHAR(10) NULL DEFAULT NULL,
  `time2` VARCHAR(10) NULL DEFAULT NULL,
  `day3` VARCHAR(10) NULL DEFAULT NULL,
  `time3` VARCHAR(10) NULL DEFAULT NULL,
  `reg_people` INT NULL DEFAULT 0,
  `max_people` INT NULL DEFAULT 0,
  PRIMARY KEY (`subject_id`, `term`),
  UNIQUE INDEX `subject_id_UNIQUE` (`subject_id` ASC) VISIBLE,
  UNIQUE INDEX `term_UNIQUE` (`term` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `db_teamproject`.`student_grade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`student_grade` (
  `student_id` VARCHAR(12) NOT NULL,
  `subject_id` VARCHAR(100) NOT NULL,
  `term` VARCHAR(10) NOT NULL,
  `grade` VARCHAR(10) NULL DEFAULT NULL,
  INDEX `fk_student_grade_student1_idx` (`student_id` ASC) VISIBLE,
  PRIMARY KEY (`student_id`, `subject_id`),
  INDEX `fk_student_grade_subject1_idx` (`subject_id` ASC) VISIBLE,
  CONSTRAINT `fk_student_grade_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `db_teamproject`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_grade_subject1`
    FOREIGN KEY (`subject_id`)
    REFERENCES `db_teamproject`.`subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `db_teamproject`.`subject_eval`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`subject_eval` (
  `eval_id` VARCHAR(45) NOT NULL,
  `subject_id` VARCHAR(100) NOT NULL,
  `term` VARCHAR(10) NOT NULL,
  `subject_eval` VARCHAR(2000) NOT NULL,
  `eval_score` DOUBLE NULL,
  PRIMARY KEY (`eval_id`, `subject_id`),
  INDEX `fk_subject_eval_subject1_idx` (`term` ASC) VISIBLE,
  CONSTRAINT `fk_subject_eval_subject`
    FOREIGN KEY (`subject_id`)
    REFERENCES `db_teamproject`.`subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_subject_eval_subject1`
    FOREIGN KEY (`term`)
    REFERENCES `db_teamproject`.`subject` (`term`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `db_teamproject`.`prerequisite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`prerequisite` (
  `prerequisite_id` VARCHAR(20) NOT NULL,
  `subject_name` VARCHAR(50) NOT NULL,
  `pre_subject_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`prerequisite_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `db_teamproject`.`score`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`score` (
  `score_id` VARCHAR(20) NOT NULL,
  `student_id` VARCHAR(12) NOT NULL,
  `term` VARCHAR(10) NULL,
  `grade` INT NULL,
  PRIMARY KEY (`score_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_teamproject`.`attend`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`attend` (
  `attend_id` INT NOT NULL,
  `student_id` VARCHAR(12) NOT NULL,
  `subject_id` VARCHAR(10) NOT NULL,
  `term` VARCHAR(10) NULL,
  `score` VARCHAR(10) NULL,
  PRIMARY KEY (`student_id`, `subject_id`),
  INDEX `fk_attend_subject1_idx` (`subject_id` ASC) VISIBLE,
  UNIQUE INDEX `subject_id_UNIQUE` (`subject_id` ASC) VISIBLE,
  UNIQUE INDEX `student_id_UNIQUE` (`student_id` ASC) VISIBLE,
  CONSTRAINT `fk_attend_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `db_teamproject`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_attend_subject1`
    FOREIGN KEY (`subject_id`)
    REFERENCES `db_teamproject`.`subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_teamproject`.`announce`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`announce` (
  `subject_id` VARCHAR(20) NOT NULL,
  `announce_id` VARCHAR(10) NOT NULL,
  `announce_title` VARCHAR(20) NOT NULL,
  `announce_content` VARCHAR(500) NOT NULL,
  `announce_writer` VARCHAR(20) NULL,
  `announce_date` DATETIME NOT NULL,
  `announce_file` VARCHAR(450) NULL,
  PRIMARY KEY (`subject_id`, `announce_id`),
  CONSTRAINT `fk_announce_subject1`
    FOREIGN KEY (`subject_id`)
    REFERENCES `db_teamproject`.`subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_teamproject`.`friend`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_teamproject`.`friend` (
  `friend_id` VARCHAR(12) NOT NULL,
  `student_id` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`friend_id`, `student_id`),
  INDEX `fk_friend_student1_idx` (`student_id` ASC) VISIBLE,
  CONSTRAINT `fk_friend_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `db_teamproject`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
