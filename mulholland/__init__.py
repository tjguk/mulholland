import os, sys

quotes_path = os.path.join(os.path.dirname(__file__), "quotes")

def hello(name):
    print("Hello, %s!" % name)

def quote(author):
    with open(os.path.join(quotes_path, "%s.txt" % author.lower())) as f:
        print(f.read())
