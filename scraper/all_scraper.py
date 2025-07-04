import requests
from bs4 import BeautifulSoup


def all_category(url_general):
    """Retrieve all book categories from the home page."""
    response = requests.get(url_general)

    if response.status_code != 200:
        print("Error loading page", response.status_code)
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    all_categories = []

    nav_list = soup.find("ul", class_="nav nav-list")
    category_list = nav_list.find("ul")
    categories = category_list.find_all("li")

    for cat in categories:
        a = cat.find("a")
        href = a["href"]
        name = a.text.strip()
        full_url = "https://books.toscrape.com/" + href
        all_categories.append((name, full_url))

    return all_categories
