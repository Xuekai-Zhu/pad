def solution():
    """Liz bought a recipe book that cost $6, a baking dish that cost twice as much, five ingredients that cost $3 each, and an apron that cost a dollar more than the recipe book. Collectively, how much in dollars did Liz spend?"""
    recipe_book = 6
    baking_dish = 2 * recipe_book
    ingredients = 5 * 3
    apron = recipe_book + 1
    total_spent = recipe_book + baking_dish + ingredients + apron
    result = total_spent
    return result

print(solution())