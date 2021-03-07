import bs4
import requests
import pandas as pd
import csv

def request(web_page, pages, name):
    responses = []
    for i in range(1, pages):
        response = requests.get(web_page.format(i))
        responses.append(response)
    
    soups = []
    for i in range(len(responses)):
        soup = bs4.BeautifulSoup(responses[i].text, "html.parser")
        soups.append(soup)

    titles_books(name, soups)

def titles_books(name, soups):
    titles_book = []
    for i in range(len(soups)):
        titles = soups[i].select(name)
        for title in titles:
            titles_book.append(title.string)

    prices_books(price, soups, titles_book)

def prices_books(price, soups, titles_book):
    prices_book = []
    for i in range(len(soups)):
        prices = soups[i].select(price)
        for price_1 in prices:
            prices_book.append(price_1.text)

    to_csv(titles_book, prices_book, web_name)

def to_csv(titles_book, prices_book, web_name):
    idx = []
    for i in range(1, len(prices_book) + 1):
        idx.append(i)

    df = pd.DataFrame({"idx":idx, "name":titles_book, "price":prices_book})
    if page != 1:
        df["price"] = df["price"].apply(lambda name: name.split("\n")[0])
    export_csv = df.to_csv(r'C:\Users\Amylkar\Anaconda31\envs\platzi_data\books\{}_data.csv'.format(web_name), encoding='utf-8', index = None, header=True)


if __name__ == '__main__':
    page = int(input("Choose the site you want to extract. buscalibre = 1, linio = 0: "))

    if page == 1:
        web_page = "https://www.buscalibre.com.co/libros/categoria-novela/74?page={}"
        web_name = "buscalibre"
        pages = 13
        name = "div.nombre"
        price = "div.precioAhora"
    else:
        web_page = "https://www.linio.com.co/c/libros/literatura-y-novelas?page={}"
        web_name = "linio"
        pages = 18
        name = "span.title-section"
        price = "span.price-main"

    request(web_page, pages, name)






