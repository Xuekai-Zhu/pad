def solution():
    recipe_book = 6
    baking_dish = recipe_book * 2
    ingredient_cost = 3
    ingredients = 5
    apron = recipe_book + 1
    total_cost = recipe_book + baking_dish + (ingredient_cost * ingredients) + apron
    result = total_cost
    return result

print(solution())