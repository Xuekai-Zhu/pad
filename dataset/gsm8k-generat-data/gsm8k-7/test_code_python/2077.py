def solution():
    recipe_book_cost = 6
    baking_dish_cost = recipe_book_cost * 2
    ingredient_cost = 3
    num_ingredients = 5
    apron_cost = recipe_book_cost + 1

    # Calculate the total cost of all ingredients
    total_ingredient_cost = ingredient_cost * num_ingredients

    # Calculate the total cost of all items
    total_cost = recipe_book_cost + baking_dish_cost + total_ingredient_cost + apron_cost
    result = total_cost
    return result

print(solution())