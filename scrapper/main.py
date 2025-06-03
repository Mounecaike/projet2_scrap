import csv
import requests
from bs4 import BeautifulSoup

# 1. Scrap une page de livre
def scrapbook(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("div", class_="product_main").find("h1").text
        price = soup.find("div", class_="product_main").find("p", class_="price_color").text
        stock = soup.find("div", class_="product_main").find("p", class_="instock availability").text.strip()
        img = soup.find("div", class_="item active").find("img")["src"]
        img = "https://books.toscrape.com/" + img.replace("../", "")
        rating_tag = soup.find("p", class_="star-rating")
        rating = rating_tag["class"][1]
        description = soup.find("article", class_="product_page").find("p").text
        breadcrumb = soup.find("ul", class_="breadcrumb")
        items = breadcrumb.find_all("li")
        category = items[2].text.strip()

        table = soup.find("table", class_="table table-striped")
        rows = table.find_all("tr")
        data = {}
        for row in rows:
            header = row.find("th").text
            value = row.find("td").text
            data[header] = value
        upc = data["UPC"]
        price_incl = data["Price (incl. tax)"]
        price_excl = data["Price (excl. tax)"]

        return {
            "title": title,
            "price": price,
            "price_incl": price_incl,
            "price_excl": price_excl,
            "stock": stock,
            "rating": rating,
            "description": description,
            "category": category,
            "upc": upc,
            "image_url": img
        }
    else:
        print("Erreur lors du chargement de la page", response.status_code)

# 2. Scrap tous les livres d’une catégorie
def books_category_scrap(category_url):
    response = requests.get(category_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = []
        h3_elements = soup.find_all("h3")
        for h3 in h3_elements:
            relative_url = h3.find("a")["href"]
            full_url = "https://books.toscrape.com/catalogue/" + relative_url.replace("../", "")
            links.append(full_url)
        return links
    else:
        print("Erreur au chargement de la page", response.status_code)
        return []

# 3. Scrap toutes les catégories
def all_category(url_general):
    response = requests.get(url_general)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        all_categories = []
        nav_list = soup.find("ul", class_="nav nav-list")
        category_list = nav_list.find("ul")
        categories = category_list.find_all("li")

        for cat in categories:
            a = cat.find("a")
            href = a["href"]
            name = a.text.strip().lower().replace(" ", "_")  # propre pour nom de fichier
            full_url = "https://books.toscrape.com/" + href
            all_categories.append((name, full_url))

        return all_categories
    else:
        print("Erreur de chargement de la page :", response.status_code)
        return []

# 4. Exécution
if __name__ == "__main__":
    categories = all_category("https://books.toscrape.com/")

    for category_name, category_url in categories:
        book_urls = books_category_scrap(category_url)

        with open(f"../data/{category_name}.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "title", "price", "price_incl", "price_excl", "stock",
                "rating", "description", "category", "upc", "image_url"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for book_url in book_urls:
                data = scrapbook(book_url)
                writer.writerow(data)
