import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"
CSV_FILE = "books.csv"

def download_page(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print("Помилка завантаження:", error)
        return None

def get_rating(book):
    tag = book.find("p", class_="star-rating")
    if tag is None: return "Невідомо"
    ratings = {"One": "1 з 5", "Two": "2 з 5", "Three": "3 з 5",
               "Four": "4 з 5", "Five": "5 з 5"}
    for value in tag.get("class", []):
        if value in ratings:
            return ratings[value]
    return "Невідомо"

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = []
    blocks = soup.find_all("article", class_="product_pod")
    for block in blocks:
        title_tag = block.find("h3").find("a")
        price_tag = block.find("p", class_="price_color")
        if title_tag is None or price_tag is None:
            continue
        title = title_tag.get("title", "Назва невідома")
        price_text = price_tag.get_text(strip=True).replace("Â", "").replace("£", "")
        try:
            price = float(price_text.strip())
        except ValueError:
            price = 0.0
        books.append({"title": title, "price": price, "rating": get_rating(block)})
    return soup, books

def show_title(soup):
    tag = soup.find("title")
    print("Заголовок сайту:", tag.get_text(strip=True) if tag else "Заголовок не знайдено.")

def show_books(books):
    if not books: print("Книг не знайдено."); return
    for number, book in enumerate(books, start=1):
        print(f"{number}. {book['title']}")
        print(f"   Ціна: £{book['price']:.2f}")
        print(f"   Рейтинг: {book['rating']}")
        print("-" * 40)

def search_books(books):
    word = input("Введіть слово для пошуку: ").strip().lower()
    if not word: print("Введіть слово для пошуку."); return
    result = [book for book in books if word in book["title"].lower()]
    show_books(result)

def filter_by_price(books):
    try:
        limit = float(input("Максимальна ціна у фунтах: "))
    except ValueError:
        print("Введіть ціну числом.")
        return
    if limit < 0: print("Ціна не може бути від'ємною."); return
    result = [book for book in books if book["price"] <= limit]
    show_books(result)

def show_statistics(books):
    if not books: print("Немає даних для статистики."); return
    prices = [book["price"] for book in books]
    cheapest = min(books, key=lambda item: item["price"])
    expensive = max(books, key=lambda item: item["price"])
    print("Кількість книг:", len(books))
    print(f"Середня ціна: £{sum(prices) / len(prices):.2f}")
    print("Найдешевша:", cheapest["title"], f"(£{cheapest['price']:.2f})")
    print("Найдорожча:", expensive["title"], f"(£{expensive['price']:.2f})")

def save_csv(books):
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as file:
            columns = ["title", "price", "rating"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for book in books:
                writer.writerow(book)
        print("Збережено файл:", CSV_FILE)
    except OSError as error:
        print("Помилка запису файлу:", error)

def show_menu():
    print("\nМЕНЮ ПАРСЕРА КНИГ")