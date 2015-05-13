__author__ = 'Travis'


def new_recipe():
    """gathers a list of ingredients for a new recipe"""

    ingredients_list = []
    print "Let's start by entering the ingredients for the new recipe."
    print "When finished type the word done on any prompt."
    while True:
        ingredient = raw_input("Enter quantity and ingredient name here: ")
        if ingredient == 'done':
            break
        else:
            ingredients_list.append(ingredient)
    return ingredients_list


def new_recipe_function():
    """creates a new recipe .txt file"""

    print "Type the word done to exit at any point."
    recipe_name = raw_input("Enter the recipe name without capital letters here: ")
    if recipe_name != 'done':
        recipe_name += '.txt'
        ingredients = new_recipe()
        recipe_file = open(recipe_name, 'w')
        recipe_file.write(recipe_name)
        recipe_file.write('\n' * 2)
        recipe_file.write('Ingredients:\n')
        for i in ingredients:
            recipe_file.write(i)
            recipe_file.write('\n')
        recipe_file.close()
