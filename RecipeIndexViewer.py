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

    path = os.curdir
    recipe = raw_input("What is the name of the recipe you want to view (don't use capital letters)? ")
    recipe += '.txt'
    if recipe in path:
        output = open(recipe)
        print output.read()
        output.close()
    else:
        print "recipe was not found, please check your spelling."
        pass