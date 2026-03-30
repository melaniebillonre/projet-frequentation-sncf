import requests
import os

# URL du dataset fréquentation des gares SNCF (open data officiel)
URL = "https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/frequentation-gares/exports/csv?delimiter=%3B&lang=fr&timezone=Europe%2FParis"

# Dossier de destination
RAW_FOLDER = "data/raw"
FILE_NAME = "frequentation_gares.csv"


def download_data():
    print("Téléchargement des données SNCF...")
    
    os.makedirs(RAW_FOLDER, exist_ok=True)
    
    response = requests.get(URL)
    
    if response.status_code == 200:
        filepath = os.path.join(RAW_FOLDER, FILE_NAME)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Fichier sauvegardé : {filepath}")
    else:
        print(f"❌ Erreur {response.status_code} : impossible de télécharger les données")


if __name__ == "__main__":
    download_data()
