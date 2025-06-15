# 📚 Projet de Web Scraping - Books to Scrape

Ce projet a été réalisé dans le cadre de la formation Développeur d’application Python (OpenClassrooms).

Il permet de :
- Scraper toutes les catégories du site [Books to Scrape](https://books.toscrape.com)
- Extraire les données de chaque livre (titre, prix, stock, description, etc.)
- Télécharger les images associées
- Générer un fichier CSV par catégorie dans le dossier `/data`
- Sauvegarder les images dans le dossier `/images`

---

## 🛠 Technologies utilisées

- Python 3.x
- `requests`
- `beautifulsoup4`
- `csv` (librairie standard Python)

---

## 📦 Installation

1. Clone ce dépôt ou télécharge-le en `.zip`

```bash
git clone https://github.com/votre-nom-utilisateur/nom-du-repo.git
cd nom-du-repo
```

2. Installe les dépendances avec `pip` :

```bash
pip install -r requirements.txt
```

---

## 🚀 Mise en route

### 1. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
```

### 2. Activer l’environnement virtuel

- **Windows** :

```bash
venv\Scripts\activate
```

- **macOS/Linux** :

```bash
source venv/bin/activate
```

### 3. Lancer le scraping complet

```bash
python main.py
```

Les fichiers CSV générés seront enregistrés dans le dossier `data/`  
Les images seront téléchargées dans le dossier `images/`

---


## 📁 Structure du projet

```
📦 projet/
├── main.py                  # Point d’entrée principal
├── demo_etl.py              # Démo du pipeline ETL (optionnel)
├── scraper/
│   ├── __init__.py
│   ├── all_scraper.py       # Fonction all_category()
│   ├── book_scraper.py      # Fonction scrapbook() + download_image()
│   └── category_scraper.py  # Fonction books_category_scrap()
├── data/                    # Dossiers des fichiers CSV (générés)
├── images/                  # Dossiers des images téléchargées (générés)
├── requirements.txt         # Dépendances du projet
└── README.md
```
