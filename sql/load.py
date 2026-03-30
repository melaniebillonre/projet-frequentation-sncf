import pandas as pd
import sqlite3
import os

CLEAN_FILE = "data/clean/frequentation_gares_clean.csv"
DB_PATH = "data/sncf_frequentation.db"


def load_to_sqlite():
    print("📦 Chargement des données dans SQLite...")

    df = pd.read_csv(CLEAN_FILE, sep=";", encoding="utf-8")

    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    df.to_sql("frequentation_gares", conn, if_exists="replace", index=False)

    print(f"✅ {len(df)} lignes chargées dans la base")

    # Vérification
    result = pd.read_sql("SELECT COUNT(*) as total FROM frequentation_gares", conn)
    print(f"✅ Vérification : {result['total'][0]} lignes en base")

    conn.close()


if __name__ == "__main__":
    load_to_sqlite()