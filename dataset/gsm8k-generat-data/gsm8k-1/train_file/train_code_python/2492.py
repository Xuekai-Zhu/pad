def solution():
    """The recipe for a four-person cake requires 2 eggs and 4 cups of milk. Tyler wants to use this recipe to make a cake for eight people. If Tyler has 3 eggs in the fridge, how many more eggs does Tyler need to buy?"""
    recipe_servings = 4
    recipe_eggs = 2
    desired_servings = 8
    eggs_needed = (desired_servings / recipe_servings) * recipe_eggs - 3
    result = eggs_needed
    return result

print(solution())