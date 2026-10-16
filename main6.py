
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("title")
print("Заголовок сайту:", title.text)

books = soup.find_all("article", class_="product_pod")

print("\nПерші 5 книг:")

for book in books[:5]:
    name = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text

    print("Назва:", name)
    print("Ціна:", price)
    print("--------------------")
