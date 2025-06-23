# 📚 Web Scraping Project - Books to Scrape

This project was built as part of the OpenClassrooms Python Developer training.

It allows you to:
- Scrape all categories from the [Books to Scrape](https://books.toscrape.com) website  
- Extract data from each book (title, price, stock, description, etc.)  
- Download the associated images  
- Generate one CSV file per category in the `/data` folder  
- Save images in the `/images` folder  

---

## 🛠 Technologies Used

- Python 3.x  
- `requests`  
- `beautifulsoup4`  
- `csv` (Python standard library)  

---

## 📦 Installation

1. Clone this repository or download it as a `.zip`:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

```

2. Install the dependencies using pip :

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 2. Activate the virtual environment

- **Windows** :

```bash
venv\Scripts\activate
```

- **macOS/Linux** :

```bash
source venv/bin/activate
```

### 3. Run the full scraping process

```bash
python main.py
```

The generated CSV files will be saved in the data/ folder
The images will be downloaded into the images/ folder

---


## 📁 Project Structure

```
📦 project/
├── main.py                  # Main entry point
├── scraper/
│   ├── __init__.py
│   ├── all_scraper.py       # Function all_category()
│   ├── book_scraper.py      # Function scrapbook() + download_image()
│   └── category_scraper.py  # Function books_category_scrap()
├── data/                    # Folder for generated CSV files
├── images/                  # Folder for downloaded images
├── requirements.txt         # Project dependencies
└── README.md

```
