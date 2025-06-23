import requests
from bs4 import BeautifulSoup


def books_category_scrap(category_url):
    """Scrape all book links from a given category with pagination."""
    all_links = []

    while category_url:  # As long as there is one page left to go
        response = requests.get(category_url)

        if response.status_code != 200:
            print("Error loading page", response.status_code)
            break

        soup = BeautifulSoup(response.content, "html.parser")

        # Retrieving book links on this page
        h3_elements = soup.find_all("h3")
        for h3 in h3_elements:
            relative_url = h3.find("a")["href"]
            full_url = (
                "https://books.toscrape.com/catalogue/"
                + relative_url.replace("../", "")
            )
            all_links.append(full_url)

        # Checking a next page
        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_page = next_btn.find("a")["href"]
            base_url = category_url.rsplit("/", 1)[0]
            category_url = base_url + "/" + next_page
        else:
            category_url = None  # End of pagination

    return all_links
