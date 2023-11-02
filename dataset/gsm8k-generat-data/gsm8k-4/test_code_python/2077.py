def solution():
    """Liz bought a recipe book that cost $6, a baking dish that cost twice as much, five ingredients that cost $3 each, and an apron that cost a dollar more than the recipe book. Collectively, how much in dollars did Liz spend?"""
    # Define the cost of each item
    recipe_book_cost = 6
    baking_dish_cost = recipe_book_cost * 2
    ingredient_cost = 3
    apron_cost = recipe_book_cost + 1

    # Calculate the total cost of the purchase
    total_cost = recipe_book_cost + baking_dish_cost + (5 * ingredient_cost) + apron_cost

    # return the result
    result = total_cost
    return result

print(solution())