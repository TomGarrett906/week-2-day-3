def shopping_cart():
    food_item = {}

    while True:
        item = input("What do you want to add to your cart? \n or [q]uit: ")
        if item.lower() in ('q','quit'):
            break
        amount = input(f"How many {item}'s would you like? ")
        food_item[item] = amount
    return food_item

print(shopping_cart())