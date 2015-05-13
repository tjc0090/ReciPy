__author__ = 'Travis'


import os


def index_viewer():
    """prints out a list of recipe names"""

    path = 'C:\Users\Jamie\PycharmProjects\ReciPy'
    for item in os.listdir(path):
        if item.endswith(".txt"):
            print item


def recipe_printer():
    """prints out an individual recipe in full"""

    recipe = raw_input("What is the name of the recipe you want to view (don't use capital letters? ")
    recipe += '.txt'
    output = open(recipe)
    print output.read()
    output.close()