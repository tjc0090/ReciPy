__author__ = 'Travis'


import RecipeIndexViewer
import ReciPyInput
import ReciPyEditDel
import GroceryList


def intro():
    """introduction for user on what program is, calls main menu"""

    print """Welcome to the ReciPy recipe card index. This program will enable you to store your recipes for easy access,
    enter new recipes whenever you come across one worth keeping, delete ones you are no longer using, and generate
    a grocery list based on your meal plan. ***Please note this is still very much a huge work in progress!***"""
    while True:
        commands()


def commands():
    """general commands and main menu for user, will reprint as necessary"""

    print """Use the following selections to make your commands as needed:
    press Ctrl + c to exit the program at any point, beware this may not save your data!
    Enter the appropriate number to execute any of the following commands:
    1. Enter a new recipe
    2. View an existing recipe
    3. View a list of all existing recipes
    4. Safely exit the program
    5. Delete a recipe
    6. Create a grocery list"""

    choice = raw_input("Enter your selection here: ")

    if choice == '1':
        ReciPyInput.new_recipe_function()
    elif choice == '2':
        RecipeIndexViewer.recipe_printer()
    elif choice == '3':
        RecipeIndexViewer.index_viewer()
    elif choice == '4':
        raise SystemExit
    elif choice == '5':
        ReciPyEditDel.del_recipe()
    elif choice == '6':
        print GroceryList.ingredients_list()
    else:
        print "Input was invalid, please try again."


intro()
