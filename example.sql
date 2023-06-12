###Structure###

use skillbox;

show tables;

DESCRIBE Courses\G

INSERT INTO Courses (name, duration, price, teacher_id) VALUES("SQL", 20, 40000, 3);

UPDATE Courses SET price = price * 0.95 WHERE type = "DESIGN";

CREATE TABLE PurchaseList (
student_name VARCHAR(200),
course_name VARCHAR(200),
price INT,
subscription_date DATETIME);

INSERT INTO PurchaseList(student_name, course_name, subscription_date, price) SELECT Students.name AS student_name,
Courses.name AS course_name, Subscription_date, price FROM Courses
JOIN Subscriptions ON Subscriptions.course_id = Courses.id
JOIN Students ON Students.id = Subscriptions.student_id;

ALTER TABLE Courses ADD COLUMN price_per_hour FLOAT;
UPDATE Course SET price_per_hour = price/duration;

---Basic_functions---

SELECT DISTINCT type FROM Courses;

SELECT name, students_count FROM Courses WHERE type = "PROGRAMMING" ORDER BY price DESC, duration ASC;

SELECT name FROM Students
UNION
SELECT name FROM Teachers;

SELECT registration_date, DATEDIFF(NOW(), registration_date) AS days_since_registration FROM Students LIMIT 10;

SELECT name, IF(students_count > 100, "FULL", "NOT FULL") AS Status FROM Courses ORDER BY Status DESC;

SELECT CONCAT("Please buy our new course '", name, "' It's only ", duration, " hours long, and the price is ", price, " rub.") FROM Courses LIMIT 10;

SELECT SUM(duration), MAX(students_count), MIN(price) FROM Courses;

SELECT Teachers.name AS teacher_name, AVG(Students.age) AS student_age
FROM Subscriptions 
JOIN Students ON Subscriptions.student_id = Students.id
JOIN Courses ON Courses.id = Subscriptions.course_id
JOIN Teachers ON Courses.teacher_id = Teachers.id
WHERE Students.age < 35
GROUP BY Teachers.name
ORDER BY Teachers.name;
