__author__ = 'Travis'


def recipe_fetcher():
    """retrieves a list of recipe .txt files"""

    meal_plan = []
    print "Type 'done' when you are finished adding recipes to your meal plan."
    done = False
    while not done:
        recipe = raw_input("Please enter the name of the recipe, the ingredients will be added to your grocery list: ")
        if recipe == 'done':
            break
        else:
            print "Recipe has been added to your meal plan!"
            recipe += '.txt'
            meal_plan.append(recipe)
    return meal_plan


def ingredients_list():
    """returns a list of all the ingredients for the selected recipies"""

    meal_plan = recipe_fetcher()
    grocery_list = []
    for entry in meal_plan:
        recipe = open(entry)
        for line in recipe:
            if 'Ingredients' in line or '.txt' in line or len(line) < 3:
                pass
            else:
                line = line.rstrip('\n')
                grocery_list.append(line)
        recipe.close()
    return grocery_list




