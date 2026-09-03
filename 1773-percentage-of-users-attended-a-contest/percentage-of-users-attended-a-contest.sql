# Write your MySQL query statement belo
SELECT
    contest_id,
    ROUND(COUNT(DISTINCT(r.user_id)) * 100 / (SELECT COUNT(*) FROM Users),2)
    AS percentage
FROM
    Register AS r
GROUP BY 
        contest_id
ORDER BY 
        percentage DESC, r.contest_id