import os.path


class Book:
    def __init__(self, title, authors, rating, read):  # constructor - object initialisation
        self.title = title  # self - reference to created object - new declarations container
        self.authors = authors
        self.rating = rating
        self.read = read
        self.set_rating(rating)
        self.set_read(read)

    def set_rating(self, value):
        if 1.0 <= value <= 10.0:
            self.rating = value
        else:
            print("Improper rating - rating set as default - 0\n Modify it if you want")
            self.rating = 0

    def set_read(self, value):
        if value == "True" or value == True:
            self.read = True
        elif value == "False" or value == False:
            self.read = False
        else:
            print("Improper read status - read status set as default - False \n Modify it if you want")


class BookBot:
    def __init__(self):
        self.shelf = []

# -----=------ Bot interaction functionalities -----=------

    def introduce(self):
        print("\nHi, Im bot Olivier - I will assist you. Pick what you want to do: ")
        self.load_books()
        self.help()
        self.options()

    def help(self):
        print("\n Commands: ")
        print("Add - Add new book")
        print("List - List books from shelf")
        print("Modify - Choose a book and change record")
        print("View rating - filter shelf by books rating from  defined scope")
        print("View read - filter shelf by read books")
        print("Save - Save database to csv file")
        print("Help - View available commands")
        print("Exit - Say goodbye to Olivier")

    def options(self):
        text = input("\nWhat I need to do? ")
        if text == "Add":
            self.input_add_book()
        elif text == "List":
            self.list_books()
        elif text == "Modify":
            self.pick_book_change()
        elif text == "View rating":
            self.filter_rating()
        elif text == "View read":
            self.filter_read()
        elif text == "Save":
            self.save_books()
        elif text == "Help":
            self.help()
            self.options()
        elif text == "Exit":
            exit()
        else:
            self.repeat()

    def repeat(self):
        print("Unrecognised operation, try again")
        self.options()

# -----=------ Adding items to list -----=------

    def add_book(self, title, authors, rating, read):
        b = Book(title, authors, rating, read)  # create object Book
        self.shelf.append(b)  # add to list

   # def insert_book(self):
   #     self.add_book("Pan Tadeusz", "Adam Mickiewicz", 1, False)
   #     self.add_book("Splatana Siec", "Michal Zalewski", 10, True)

    def input_add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        rating = float(input("Rating: "))
        read = input("Read? ")

        self.add_book(title, author, rating, read)
        print("--------------------------")
        self.options()

# -----=------ Modify items in list -----=------

    def pick_book_change(self):
        print("\nPick up book what you want to change!")
        index = int(input("Index: "))
        try:
            book = self.shelf[index - 1]
        except IndexError:
            print("You overlapped index in shelf - try again with proper index.")
            self.options()
        else:
            self.change_record(book)

    def change_record(self, book):
        choice = input("\nWhat do you want to change? ")
        if choice == "Title":
            book.title = input("Insert new title: ")
        elif choice == "Author":
            book.authors = input("Insert new author: ")
        elif choice == "Rating":
            book.set_rating(float(input("Insert new rating: ")))
        elif choice == "Read":
            book.set_read(input("Insert new read status True/False: "))
        else:
            print("Unknown value - try again")
        print("--------------------------")
        self.options()

# -----=------ Print books -----=------

    def print_book(self, index):
        book = self.shelf[index]
        print("{:4} | {:30} | {:30} | {:5} | {:5}".format(index, book.title, book.authors, book.rating, book.read))

    def list_books(self):
        print("\n--------------------------")
        for index in range(len(self.shelf)):
            self.print_book(index)
        print("--------------------------")
        self.options()

    def print_all_read_book(self, choice):
        print("\n--------------------------")
        for i in range(len(self.shelf)):
            book = self.shelf[i]
            if choice == 1:
                if book.read:
                    self.print_book(i)
            else:
                if not book.read:
                    self.print_book(i)
        print("--------------------------")

    def print_all_rating_books(self, min, max):
        print("\n--------------------------")
        for i in range(len(self.shelf)):
            book = self.shelf[i]
            if min <= book.rating <= max:
                self.print_book(i)
        print("--------------------------")

# -----=------ Filtering options -----=------

    def filter_rating(self):
        print("Rating value scope - 1.0 - 10.0 \nUnset value - 0")
        min = float(input("Min rating value: "))
        max = float(input("Max rating value: "))
        if min >= 1.0 and max <= 10.0:
            self.print_all_rating_books(min, max)
            self.options()
        else:
            print("Improper rating value - try again")
            self.options()

    def filter_read(self):
        print("Sort by: \n read - 1 \n unread - 0")
        choice = int(input("\n Choose (1 or 0): "))
        if 0 >= choice or choice <= 1:
            self.print_all_read_book(choice)
            self.options()
        else:
            print("Improper read value - try again")
        self.options()

# -----=------ Load/Save items in list (file) -----=------

    def save_books(self):
        text_holder = []
        for i in range(len(self.shelf)):
            book = self.shelf[i]
            text = "{};{};{};{}".format(book.title, book.authors, book.rating, book.read)
            text_holder.append(text)
        with open('books.csv', 'w') as f:
            for line in text_holder:
                f.write(line + '\n')
        self.options()

    def load_books(self):
        if os.path.isfile('./books.csv'):
            with open('books.csv', 'r') as f:
                for line in f:
                    book_list = line.split(';')
                    if book_list[3] == 'True\n':
                        read = True
                    else:
                        read = False
                    self.add_book(book_list[0], book_list[1], float(book_list[2]), read)
            print("\nDatabase loaded!\n")


bot = BookBot()
bot.introduce()

