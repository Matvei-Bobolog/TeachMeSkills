-- 📄 Примеры команд SQL (подсказки):
-- ===========================
-- Как создать таблицу:
-- CREATE TABLE table_name (
--     column1 datatype,
--     column2 datatype,
--     ...
-- );

-- Как вставить данные:
-- INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');

-- Как обновить данные:
-- UPDATE table_name SET column1 = 'new_value' WHERE some_condition;

-- Как добавить новый столбец:
-- ALTER TABLE table_name ADD COLUMN column_name datatype;

-- Как удалить таблицу:
-- DROP TABLE table_name;

-- ===========================
-- 📋 Задания (выполняйте TODO):
-- ===========================


-- ✅ TODO 1: Создайте таблицу "Employees" с полями:
-- Name (TEXT), Position (TEXT), Department (TEXT), Salary (NUMERIC)

CREATE TABLE Employees (
    -- id INT AUTO_INCREMENT PRIMARY KEY,
    `Name` TEXT,
    Position TEXT,
    Department TEXT,
    Salary INT
);


-- ✅ TODO 2: Вставьте несколько записей в таблицу "Employees"

INSERT INTO Employees (`Name`, Position, Department, Salary) VALUES ('Yegor', 'Manager', 'Sales', 3600), ('Igor', 'Janitor', 'Cleaning', 1100), ('Yaropolk', 'CEO', 'Finances', 12900);


-- ✅ TODO 3: Измените должность одного из сотрудников на более высокую

UPDATE Employees SET Position = 'Doorman', Salary = 1200 WHERE `Name` = 'Yegor';


-- ✅ TODO 4: Добавьте новое поле "HireDate" (DATE) в таблицу "Employees"

ALTER TABLE Employees ADD COLUMN HireDate DATE;


-- ✅ TODO 5: Добавьте дату приема на работу для всех сотрудников

UPDATE Employees SET HireDate = '20.10.2002' WHERE `Name` = 'Yegor';
UPDATE Employees SET HireDate = '01.01.2022' WHERE `Name` = 'Igor';
UPDATE Employees SET HireDate = '29.02.2014' WHERE `Name` = 'Yaropolk';


-- ✅ TODO 6: Найдите всех сотрудников с должностью "Manager"

SELECT * FROM Employees WHERE Position = 'Manager';


-- ✅ TODO 7: Найдите всех сотрудников с зарплатой больше 5000

SELECT * FROM Employees WHERE Salary > 5000;


-- ✅ TODO 8: Найдите всех сотрудников, которые работают в отделе "Sales"

SELECT * FROM Employees WHERE Department = 'Sales';


-- ✅ TODO 9: Найдите среднюю зарплату всех сотрудников

SELECT AVG(Salary) AS average_salary FROM Employees;


-- ✅ TODO 10: Удалите таблицу "Employees"

-- ⚠️ ВНИМАНИЕ: Эта команда удалит таблицу и все данные!
-- Выполняйте её только после того, как закончите все задания выше.

DROP TABLE Employees;


-- 🎯 *Задание с повышенным уровнем сложности:*
-- Реализуйте задачи 6–9 в виде ХРАНИМЫХ ФУНКЦИЙ или ПРОЦЕДУР.

-- Подсказка:
-- CREATE FUNCTION или CREATE PROCEDURE
-- BEGIN ... END

-- Пример вызова:
-- CALL имя_процедуры();

CREATE PROCEDURE show_managers(OUT managers TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT `Name` INTO managers FROM Employees WHERE Position = 'Manager';
END;
$$;

CALL show_managers();

CREATE PROCEDURE show_rich_ones(salary INT, OUT rich TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT `Name` INTO rich FROM Employees WHERE Salary > salary;
END;
$$;

CALL show_rich_ones(5000);

CREATE PROCEDURE show_those_in_sales(OUT people TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT `Name` INTO people FROM Employees WHERE Department = 'Sales';
END;
$$;

CALL show_those_in_sales();

CREATE FUNCTION average_salary()
RETURNS NUMERIC
AS $$
DECLARE
    Average_salary NUMERIC;
BEGIN
    SELECT AVG(Salary) INTO Average_salary FROM Employees;
    RETURN Average_salary;
END;
$$ LANGUAGE plpgsql;

CALL average_salary();