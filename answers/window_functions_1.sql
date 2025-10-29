SELECT *,
SUM(weight) OVER() AS total_weight,
FROM furniture