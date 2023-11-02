def solution():
    """Liz bought a recipe book that cost $6, a baking dish that cost twice as much, five ingredients that cost $3 each, and an apron that cost a dollar more than the recipe book. Collectively, how much in dollars did Liz spend?"""
    recipe_book_cost = 6
    baking_dish_cost = recipe_book_cost * 2
    ingredient_cost = 3
    num_ingredients = 5
    apron_cost = recipe_book_cost + 1
    
    total_cost = recipe_book_cost + baking_dish_cost + (ingredient_cost * num_ingredients) + apron_cost
    result = total_cost
    return result

print(solution())