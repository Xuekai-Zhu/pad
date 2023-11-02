def solution():
    
    recipe_servings = 4
    recipe_eggs = 2
    desired_servings = 8
    eggs_needed = (desired_servings / recipe_servings) * recipe_eggs - 3
    result = eggs_needed
    return result

print(solution())