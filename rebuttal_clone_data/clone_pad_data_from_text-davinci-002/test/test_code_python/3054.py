def solution():
    original_recipe_servings = 7
    desired_servings = 35
    original_recipe_amount = 2
    needed_amount = (original_recipe_amount / original_recipe_servings) * desired_servings
    result = needed_amount
    return result

print(solution())