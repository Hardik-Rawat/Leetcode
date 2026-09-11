# Write your MySQL query statement below
WITH cte AS
(SELECT
    person_name,
    SUM(weight) OVER(ORDER BY turn ROWS BETWEEN 
    UNBOUNDED PRECEDING AND CURRENT ROW) 
AS 
    sum_weight
FROM
    Queue)
SELECT
    person_name
FROM 
    cte
WHERE 
    sum_weight<=1000
ORDER BY
    sum_weight DESC
LIMIT 
    1

