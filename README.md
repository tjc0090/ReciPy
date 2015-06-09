# ReciPy
The goal of this program is store, edit, and delete recipes from a .txt file directory. It can then use those files to return a grocery list based on recipes chosen by the users specified input.

Currently the application can store, delete, view individual recipes as well as return a list of ingredients (grocery list)
from a selection of recipes (meal plan) that is determined by the user.

Functionality still to add:
- Combining like ingredients found in multiple recipes in a meal plan.
- Sorting the list based on category (produce, meat, dairy, etc...)
- Have the program select a random recipe
- Edit an existing recipe
- Generating and send an email containing the week's grocery list

** I am writing this application to help out my household so functions may be added/dropped based on changing wants



Troubleshooting, bugs, other issues:
- Currently error handling is good, but could be a bit better.
- All of the recipes are stored in the same directory as the .py files, this will be changed to having a new directory created and then storing all .txt (recipe) files in it instead.
- Currently the grocery list is simply printed out on the command line, that may change to writing to a file, or I may simply write the code for email generation; it really just depends on what my SO would like.
- When a command is executed the command menu is then immediately reprinted. That may change to where the user needs to press a key to have it reprinted, once again it depends on what my SO would like.
