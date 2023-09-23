pantry = {
   "chicken": 500,
   "lemon": 200,
   "cumin": 24,
   "paprika": 18,
   "chilli powder": 7,
   "yogurt": 300,
   "oil": 450,
   "onion": 5,
   "garlic": 9,
   "ginger": 2,
   "tomato puree": 125,
   "almonds": 75,
   "rice": 500,
   "coriander": 20,
   "lime": 3,
   "pepper": 8,
   "egg": 6,
   "pizza": 2,
   "spam": 1,
   "potatoes": 500,
   "salt": 1000,
   "malt vinegar": 500,
   "bread": 500,
   "butter": 250,
   "beans": 300,
   "tin opener": 100,
   "spoon": 50

}

#Dictionary2 - Recipes
recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
        ],
   "Spam a la tin": [
       "spam",
       "tin opener",
       "spoon",
   ]
}


#To update stock after recipe preparation
def pantry_stock(pantry_items):
   #print(pantry_items)
   for item in pantry_items:
       item_quantity = int(pantry.get(item))
       pantry[item] = item_quantity - 1
   print("Message from Pantry : Recipe is ready (stocks updated)")
   print("\nStock updated for below items:")
   for item in pantry_items:
       item_quantity = int(pantry.get(item))
       print(item, " = ", item_quantity)

       # main
menu = '''
       1 : Butter chicken
       2 : Chicken and chips
       3 : Pizza
       4 : Egg sandwich
       5 : Beans on toast
       6 : Spam a la tin
       '''

print(menu)
choice = input("Input a number (1 to 6) for your recipe from above menu :")

recipes_menu = list(recipes.keys())

match choice:
   case "1":
           x = recipes_menu[0]
           x_items = recipes[x]
           print("Placed Order for", x, "...")
           pantry_stock(x_items)
   case "2":
           x = recipes_menu[1]
           x_items = recipes[x]
           print("Placed Order for", x, "...")
           #print(x_items)
           pantry_stock(x_items)
   case "3":
           x = recipes_menu[2]
           x_items = recipes[x]
           print("Placed Order for", x, "...")
           pantry_stock(x_items)
   case "4":
           x = recipes_menu[3]
           x_items = recipes[x]
           print("Placed Order for", x, "...")
           pantry_stock(x_items)
   case "5":
           x = recipes_menu[4]
           x_items = recipes[x]
           print("Placed Order for", x, "...")
           pantry_stock(x_items)
   case "6":
           x = recipes_menu[5]
           x_items = recipes[x]
           print("Placed Order for", x, "...")
           pantry_stock(x_items)
   case _: print("Invalid input!")










