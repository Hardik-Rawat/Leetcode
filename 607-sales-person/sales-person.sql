# Write your MySQL query statement below
WITH cte AS
(SELECT
    DISTINCT
    o.sales_id
FROM 
    Company c
JOIN 
    Orders o
ON c.com_id=o.com_id
WHERE c.name LIKE 'RED')

SELECT
    s.name
FROM
    SalesPerson s
WHERE sales_id NOT IN(SELECT DISTINCT sales_id FROM cte)

