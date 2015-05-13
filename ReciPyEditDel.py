__author__ = 'Travis'


import os


def del_recipe():
    """deletes an existing recipe file"""

    print "Please type the name of the recipe you would like to delete. This will permanently erase the recipe."
    choice = raw_input("Recipe to delete: ")
    choice += '.txt'
    path = 'C:\Users\Jamie\PycharmProjects\ReciPy'
    recipe = os.path.join(path, choice)
    os.remove(recipe)
    print "Your selected recipe has been deleted."
