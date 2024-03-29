# Bot BoB - basic stuff


def introduce():
    bot_name = "Bob"
    print("Hi, Im bot ", bot_name)
    help()
    options()


def help():
    print("\n I can: \n * calculate - do some simple math for two numbers \n * name - asking for you name \n * join - "
          "merge two texts together \n * shopping - create a shopping list \n * note - write down you notes \n * "
          "guess - entertain you with my guess word game! \n help - list commands again \n exit - say bye to Bob! \n "
          "\n Pick one and have fun!")


def repeat():
    print("Unrecognised operation, try again")
    options()


def options():
    text = input("\n What I need to do? ")
    if text == "calculate":
        calculate()
    elif text == "name":
        name()
    elif text == "join":
        join()
    elif text == "shopping":
        shopping_list()
    elif text == "note":
        notes()
    elif text == "guess":
        guessing()
    elif text == "exit":
        exit()
    elif text == "help":
        help()
        options()
    else:
        repeat()


def calculate():
    # default input takes string from user
    a = int(input("Assign a: "))
    b = int(input("Assign b: "))
    calculate_ab(a, b)


def calculate_ab(a, b):
    print("a + b = ", a + b)
    print("a - b = ", a - b)
    print("a / b = ", a / b)  # divide, return float
    print("a // a = ", a // b)  # divide, return integer
    print("a * b = ", a * b)
    print("a % b = ", a % b)  # modulo
    print("a ** b = ", a ** b)  # power


def name():
    username_bot = input("What is your name ?")
    print("Hi ", username_bot)
    options()


def join():
    a = input("Assign string a: ")
    b = input("Assign string b: ")
    print(join_text(a, b))
    options()


def join_text(a, b):
    c = a + b
    return c


def shopping_list():
    a = []  # index start from 0
    for i in range(4):
        item = input("What I need to buy?")
        a.append(item)
    print(a)
    as_list(a)
    options()


def as_list(a):
    for item in a:
        print("Noted: ", item)
    print("END")


def notes():
    number = int(input("Number of notes:"))
    d = {}  # dictionary
    for i in range(number):
        note = input("Note: ")
        d[i] = note
    print(d)
    in_dictionary(d)
    options()


def in_dictionary(a):
    for key in a:
        print("Note ", key, ": ", a[key])
    print("END")


def guessing():
    hidden_word = "hidden"
    solved = False

    while not solved:
        user_word = input("Try to guess! ")
        if hidden_word == user_word:
            solved = True
        else:
            for letter in user_word:
                if letter in hidden_word:
                    print("Ha you missed, but your letter ", letter, " is in my word!")
                else:
                    print("Your letter ", letter, "is not in my word!")
    print("Congratz!")
    options()


introduce()
