def solution():
    recipe_servings = 4
    recipe_eggs = 2
    recipe_milk = 4

    desired_servings = 8

    eggs_available = 3

    # Calculate the ratio of servings to eggs needed in the recipe
    recipe_servings_per_egg = recipe_servings / recipe_eggs

    # Calculate the number of eggs needed for the desired number of servings
    desired_eggs = desired_servings / recipe_servings_per_egg

    # Calculate the number of additional eggs Tyler needs to buy
    eggs_needed = desired_eggs - eggs_available
    result = eggs_needed
    return result

print(solution())