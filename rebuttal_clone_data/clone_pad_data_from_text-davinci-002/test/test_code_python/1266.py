def solution():
    servings = 20
    recipe_calls_for = 1
    ounces_in_a_can = 16
    ounces_in_recipe_calls_for = 6
    cans_needed = (servings * recipe_calls_for * ounces_in_recipe_calls_for) / ounces_in_a_can
    result = cans_needed
    return result

print(solution())