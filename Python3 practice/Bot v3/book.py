import json
import os


def load_book(filename):
    with open('books/' + filename, 'r') as f:
        d = json.load(f)
        return d


def load_books():
    filenames = os.listdir('books/')
    books = []
    for filename in filenames:
        d = load_book(filename)
        books.append(d)
    return books


for book in load_books():
    print(book)


def build_book(title, authors, subtitle="", publisher="", publish_year=-1, read_date="", owner="", user="", rating=-1,
               notes=""):
    d = {
        "Title": title,
        "Subtitle": subtitle,
        "Authors": authors,
        "Publisher": publisher,
        "PublishYear": publish_year,
        "ReadDate": read_date,
        "Owner": owner,
        "User": user,
        "Rating": rating,
        "Notes": notes
    }
    return d


def save_book(book):
    title = book["Title"]
    title = title.lower()
    title = title.replace(" ", "_")
    with open("books/" + title + ".json", "w") as f:
        json.dump(book, f)


a = build_book("Pan Tadeusz", ["Adam Mickiewicz"])
print(save_book(a))
