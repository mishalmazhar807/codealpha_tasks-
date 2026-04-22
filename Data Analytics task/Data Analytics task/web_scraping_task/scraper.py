import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False)

    print("Data scraped successfully and saved to output.csv")
else:
    print("Failed to access website:", response.status_code)