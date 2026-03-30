CREATE TABLE IF NOT EXISTS frequentation_gares (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_gare TEXT NOT NULL,
    code_postal TEXT,
    direction_regionale_gares TEXT,
    segmentation_drg TEXT,
    segmentation_marketing TEXT,
    total_voyageurs_2024 INTEGER
);