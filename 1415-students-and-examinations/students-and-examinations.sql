# Write your MySQL query statement below
select s.student_id,s.student_name,su.subject_name,COUNT(e.student_id) as attended_exams
FROM students s
CROSS JOIN subjects su
LEFT JOIN examinations e
ON s.student_id = e.student_id
AND su.subject_name = e.subject_name
GROUP BY s.student_id , s.student_name , su.subject_name
ORDER BY s.student_id , s.student_name , su.subject_name ;
