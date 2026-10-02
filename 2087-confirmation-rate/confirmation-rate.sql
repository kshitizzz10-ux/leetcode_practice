# Write your MySQL query statement below
SELECT s.user_id , ROUND(avg(
                             CASE
                                 WHEN c.action = 'confirmed' THEN 1.00
                                 ELSE 0
                             END
                         ),2
                    ) as confirmation_rate
FROM signups as s
LEFT JOIN confirmations as c
ON s.user_id = c.user_id
GROUP BY user_id;