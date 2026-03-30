# projet-frequentation-sncf
Pipeline ETL sur les données de fréquentation des gares SNCF

Projet personnel pour m'entraîner au data engineering.  
Pipeline ETL sur les données open data de fréquentation des gares SNCF.

---

## Ce que fait le projet

1. Téléchargement automatique du CSV depuis data.sncf.com
2. Nettoyage des données avec Python / Pandas
3. Chargement dans une base SQLite
4. Analyse via des vues SQL

---

## Stack

- Python, Pandas
- SQLite
- DBeaver
- Git

---

## Lancer le projet

```bash
# Cloner le repo
git clone https://github.com/TON_USERNAME/sncf-frequentation-pipeline.git
cd sncf-frequentation-pipeline

# Créer l'environnement virtuel
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

# Lancer le pipeline
python ingestion/download.py
python transformation/clean.py
python sql/load.py
```

Ouvrir ensuite `data/sncf_frequentation.db` dans DBeaver et exécuter les vues depuis `sql/gold_views.sql`.

---

## Structure

```
├── ingestion/download.py        # téléchargement
├── transformation/clean.py      # nettoyage
├── sql/
│   ├── load.py                  # chargement SQLite
│   └── gold_views.sql           # vues analytiques
├── requirements.txt
└── README.md
```

---

## Quelques chiffres (données 2024)

- 3 021 gares dans le dataset
- Paris Gare du Nord : 257 millions de voyageurs
- Paris Saint-Lazare : 114 millions
- Paris Gare de Lyon : 113 millions


Source des données : [data.sncf.com](https://data.sncf.com) — licence ODbL