SELECT *, SUM(visiteurs_count) OVER(ORDER BY date) as total_visiteurs
FROM capteur_a_retrail;
