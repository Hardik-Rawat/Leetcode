# Write your MySQL query statement below
WITH cte AS
(SELECT
    product_id,
    SUM(unit) AS feb_unit
FROM
    Orders
WHERE 
    YEAR(order_date)=2020
AND MONTH(order_date)=2
GROUP BY product_id)

SELECT
    p.product_name,
    c.feb_unit AS unit
FROM cte c
LEFT JOIN Products p
ON p.product_id=c.product_id
WHERE feb_unit>=100
