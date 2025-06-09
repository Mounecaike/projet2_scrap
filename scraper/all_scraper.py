import requests
from bs4 import BeautifulSoup

def all_category(url_general):
    response = requests.get(url_general)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        all_category = []

        nav_list = soup.find("ul", class_="nav nav-list")
        category_list = nav_list.find("ul")
        categories = category_list.find_all("li")

        for cat in categories:
            a = cat.find("a")
            href = a["href"]
            name = a.text.strip()
            full_url = "https://books.toscrape.com/" + href
            all_category.append((name, full_url))

        return all_category
    else:
        print("Erreur lors du chargement de la page", response.status_code)
        return []
