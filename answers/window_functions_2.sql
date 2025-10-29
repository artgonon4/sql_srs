SELECT *,
SUM(weight) OVER(ORDER BY item) AS poids_total
FROM furniture