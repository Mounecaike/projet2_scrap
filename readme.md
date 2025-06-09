# 📚 Projet de Web Scraping - Books to Scrape

Ce projet a été réalisé dans le cadre de la formation Développeur d’application Python (OpenClassrooms).

Il permet de :
- Scraper toutes les catégories du site [Books to Scrape](https://books.toscrape.com)
- Extraire les données de chaque livre (titre, prix, stock, description, etc.)
- Télécharger les images associées
- Générer un fichier CSV par catégorie dans le dossier `/data`
- Sauvegarder les images dans le dossier `/images`

## 🛠 Technologies utilisées

- Python 3.x
- `requests`
- `beautifulsoup4`
- `csv`

## 📦 Installation

1. Clone ce dépôt ou télécharge-le en `.zip`
2. Installe les dépendances :

```bash
pip install -r requirements.txt
