def solution():
    loaves_per_recipe = 3  # Sherry's recipe makes enough batter for 3 loaves
    total_loaves = 99  # Sherry wants to make 99 loaves

    # Calculate the total number of recipes Sherry needs to make
    total_recipes = total_loaves / loaves_per_recipe

    # Calculate the number of bananas needed for all the recipes
    bananas_per_recipe = 1  # Sherry's recipe calls for 1 banana
    total_bananas = total_recipes * bananas_per_recipe
    result = total_bananas
    return result

print(solution())