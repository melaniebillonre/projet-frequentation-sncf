-- ============================================
-- VUE 1 : Top 20 des gares les plus fréquentées
-- ============================================
CREATE VIEW IF NOT EXISTS v_top20_gares AS
SELECT 
    nom_gare,
    direction_regionale_gares,
    segmentation_marketing,
    total_voyageurs_2024
FROM frequentation_gares
WHERE total_voyageurs_2024 > 0
ORDER BY total_voyageurs_2024 DESC
LIMIT 20;


-- ============================================
-- VUE 2 : Fréquentation totale par direction régionale
-- ============================================
CREATE VIEW IF NOT EXISTS v_frequentation_par_region AS
SELECT 
    direction_regionale_gares,
    COUNT(*) AS nb_gares,
    SUM(total_voyageurs_2024) AS total_voyageurs,
    ROUND(AVG(total_voyageurs_2024), 0) AS moyenne_voyageurs
FROM frequentation_gares
WHERE total_voyageurs_2024 > 0
GROUP BY direction_regionale_gares
ORDER BY total_voyageurs DESC;


-- ============================================
-- VUE 3 : Répartition par segmentation marketing
-- ============================================
CREATE VIEW IF NOT EXISTS v_frequentation_par_segment AS
SELECT 
    segmentation_marketing,
    COUNT(*) AS nb_gares,
    SUM(total_voyageurs_2024) AS total_voyageurs
FROM frequentation_gares
WHERE total_voyageurs_2024 > 0
GROUP BY segmentation_marketing
ORDER BY total_voyageurs DESC;


-- ============================================
-- VUE 4 : Gares sans voyageurs (qualité des données)
-- ============================================
CREATE VIEW IF NOT EXISTS v_gares_sans_donnees AS
SELECT 
    nom_gare,
    code_postal,
    direction_regionale_gares
FROM frequentation_gares
WHERE total_voyageurs_2024 = 0 OR total_voyageurs_2024 IS NULL;