import os
import requests
from bs4 import BeautifulSoup


def scrapbook(url):
    """Extracts all information about a book from its URL."""
    response = requests.get(url)
    if response.status_code != 200:
        print("Error loading page", response.status_code)
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("div", class_="product_main").find("h1").text
    price = soup.find("p", class_="price_color").text
    stock = soup.find("p", class_="instock availability").text.strip()

    img = soup.find("div", class_="item active").find("img")["src"]
    img = "https://books.toscrape.com/" + img.replace("../", "")

    rating = soup.find("p", class_="star-rating")["class"][1]
    description = soup.find("article", class_="product_page").find("p").text

    breadcrumb = soup.find("ul", class_="breadcrumb")
    category = breadcrumb.find_all("li")[2].text.strip()

    table = soup.find("table", class_="table table-striped")
    data = {
        row.find("th").text: row.find("td").text
        for row in table.find_all("tr")
    }

    return {
        "title": title,
        "price": price,
        "price_incl": data["Price (incl. tax)"],
        "price_excl": data["Price (excl. tax)"],
        "stock": stock,
        "rating": rating,
        "description": description,
        "category": category,
        "upc": data["UPC"],
        "image_url": img,
    }


def download_image(image_url, filename, category, folder="images"):
    """Uploads a book image to a subfolder by category."""
    category_folder = os.path.join(folder, category.lower().replace(" ", "_"))
    os.makedirs(category_folder, exist_ok=True)

    filepath = os.path.join(category_folder, filename)

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(filepath, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
    except Exception as e:
        print(f"Error downloading {image_url} : {e}")
