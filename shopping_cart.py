def shopping_cart():
    food_item = {}

    while True:

        item = input("\nWhat would you like to add to your cart?\nEnter item name or [d]elete, [q]uit: ")
        if item.lower() in ('q','quit'):
            break
 
        elif item in ('d','delete'):
            delete_item = input("What would you like to delete from your cart? ")
            if delete_item in food_item:
                delete_amount = input(f"How many {delete_item}'s would you like to delete? ")
                food_item.pop(delete_item)
                print(f"Removed {delete_amount} {delete_item}'s from cart. ")
            else:
                delete_item not in food_item
                print(f"{delete_item} not in cart. ")

        else:
            amount = input(f"How many {item}'s would you like to add? ")
            food_item[item] = amount

    return food_item

print(shopping_cart())