import csv
import requests
from bs4 import BeautifulSoup
from scraper.book_scraper import scrapbook, download_image
from scraper.category_scraper import books_category_scrap
from scraper.all_scraper import all_category


def main():
    """Main script: Retrieves data and images for each book."""
    categories = all_category("https://books.toscrape.com/")

    for category_name, category_url in categories:
        book_urls = books_category_scrap(category_url)

        csv_filename = f"data/{category_name.lower()}.csv"
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "title", "price", "price_incl", "price_excl", "stock",
                "rating", "description", "category", "upc", "image_url"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for book_url in book_urls:
                data = scrapbook(book_url)
                if data:
                    writer.writerow(data)

                    image_filename = f"{data['upc']}.jpg"
                    download_image(
                        image_url=data["image_url"],
                        filename=image_filename,
                        category=data["category"]
                    )


if __name__ == "__main__":
    main()
