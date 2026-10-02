# Write your MySQL query statement below
SELECT name
FROM Employee
WHERE id IN (select managerId FROM employee group by managerID having count(managerId) >= 5);
