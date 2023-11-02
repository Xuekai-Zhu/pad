def solution():
    recipe_book_cost = 6
    baking_dish_cost = 2 * recipe_book_cost
    ingredient_cost = 5 * 3
    apron_cost = recipe_book_cost + 1

    # Calculate the total cost of all the items
    total_cost = recipe_book_cost + baking_dish_cost + ingredient_cost + apron_cost
    result = total_cost
    return result

print(solution())