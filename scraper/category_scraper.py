import requests
from bs4 import BeautifulSoup

def books_category_scrap(category_url):
    all_links = []

    while category_url:  # Tant qu'il reste une page à parcourir
        response = requests.get(category_url)
        if response.status_code != 200:
            print("Erreur au chargement de la page", response.status_code)
            break

        soup = BeautifulSoup(response.content, "html.parser")

        # Récupération des liens des livres sur cette page
        h3_elements = soup.find_all("h3")
        for h3 in h3_elements:
            relative_url = h3.find("a")["href"]
            full_url = "https://books.toscrape.com/catalogue/" + relative_url.replace("../", "")
            all_links.append(full_url)

        # Vérification d'une page suivante
        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_page = next_btn.find("a")["href"]
            base_url = category_url.rsplit('/', 1)[0]
            category_url = base_url + '/' + next_page
        else:
            category_url = None  # Fin de la pagination

    return all_links
