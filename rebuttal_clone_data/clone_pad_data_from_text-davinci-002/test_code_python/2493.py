def solution():
    people = 8
    recipe_people = 4
    recipe_eggs = 2
    recipe_milk = 4
    eggs_needed = (people / recipe_people) * recipe_eggs
    milk_needed = (people / recipe_people) * recipe_milk
    result = eggs_needed - 3, milk_needed
    return result

print(solution())