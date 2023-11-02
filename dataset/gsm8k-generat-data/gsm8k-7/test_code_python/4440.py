def solution():
    num_loaves = 99
    loaves_per_recipe = 3
    bananas_per_recipe = 1

    # Calculate the total number of recipes required to make 99 loaves
    total_recipes = num_loaves / loaves_per_recipe

    # Calculate the total number of bananas required
    total_bananas = total_recipes * bananas_per_recipe
    result = total_bananas
    return result

print(solution())