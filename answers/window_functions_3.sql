SELECT *,
AVG(weight) OVER(ORDER BY item DESC) AS poids_total,
FROM furniture;