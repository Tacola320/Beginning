import json
import os


class IOBooks:

    def __init__(self, dirname):
        self.dirname = dirname

    def get_filename(self, book):
        return self.dirname + '/' + book

    def load_book(self, filename):
        with open(self.get_filename(filename), 'r') as f:
            d = json.load(f)
            return d

    def load_books(self):
        filenames = os.listdir(self.dirname + '/')
        books = []
        for filename in filenames:
            d = self.load_book(filename)
            books.append(d)
        return books

    def build_book(self, title, authors, subtitle="", publisher="", publish_year=-1, read_date="", owner="", user="",
                   rating=-1,
                   notes=""):
        authors = authors.split(',')
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

    def save_book(self, book):
        title = book["Title"]
        title = title.lower()
        title = title.replace(" ", "_")
        with open(self.get_filename(title) + ".json", "w") as f:
            json.dump(book, f)



