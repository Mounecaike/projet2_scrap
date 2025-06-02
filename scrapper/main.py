import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def scrapbook(url) :
    response = requests.get(url)

    if response.status_code == 200 :
        soup=BeautifulSoup(response.content, "html.parser")
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


'''
        with open("../data/single_book.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "title", "price", "price_incl", "price_excl", "stock",
                "rating", "description", "category", "upc", "image_url"
            ])
            writer.writeheader()
            writer.writerow({
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
            })
'''
data = scrapbook(url)
print(data)


