import json


with open('books/example.json', 'r') as f:
    d = json.load(f)
    print(d)
    print(d['Owner'])
