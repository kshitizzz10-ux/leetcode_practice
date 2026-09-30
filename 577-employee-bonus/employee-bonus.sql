# Write your MySQL query statement below
SELECT e.name as name , b.bonus as bonus
FROM employee as e
LEFT JOIN bonus as b
ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;