import pandas as pd
import os

RAW_FILE = "data/raw/frequentation_gares.csv"
CLEAN_FOLDER = "data/clean"
CLEAN_FILE = "frequentation_gares_clean.csv"


def load_data():
    df = pd.read_csv(RAW_FILE, sep=";", encoding="utf-8")
    print(f"✅ Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print("\nColonnes disponibles :")
    print(df.columns.tolist())
    return df


def clean_data(df):
    print("\n🧹 Nettoyage en cours...")

    # Supprimer les doublons
    df = df.drop_duplicates()

    # Supprimer les lignes sans nom de gare
    df = df.dropna(subset=["nom_gare"])

    # Nettoyer les noms de colonnes (minuscules, sans espaces)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Garder uniquement les colonnes utiles
    colonnes_utiles = [
        "nom_gare",
        "code_postal",
        "direction_regionale_gares",
        "segmentation_drg",
        "segmentation_marketing",
        "total_voyageurs_2024",
    ]
    # Ne garder que les colonnes qui existent vraiment
    colonnes_utiles = [c for c in colonnes_utiles if c in df.columns]
    df = df[colonnes_utiles]

    # Convertir total_voyageurs_2024 en nombre entier
    if "total_voyageurs_2024" in df.columns:
        df["total_voyageurs_2024"] = (
            pd.to_numeric(df["total_voyageurs_2024"], errors="coerce")
            .fillna(0)
            .astype(int)
        )

    print(f"✅ Nettoyage terminé : {df.shape[0]} lignes conservées")
    return df


def save_data(df):
    os.makedirs(CLEAN_FOLDER, exist_ok=True)
    filepath = os.path.join(CLEAN_FOLDER, CLEAN_FILE)
    df.to_csv(filepath, index=False, sep=";", encoding="utf-8")
    print(f"✅ Fichier propre sauvegardé : {filepath}")


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    save_data(df)
    print("\n📊 Aperçu des données :")
    print(df.head())