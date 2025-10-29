SELECT *, SUM(visiteurs_count) OVER() as total_visiteurs
FROM capteur_a_retrail