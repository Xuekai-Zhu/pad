def solution():
    original_recipe_servings = 7  # The original recipe serves 7 people
    reunion_servings = 35  # Dale's family reunion will have 35 people
    original_recipe_pasta = 2  # The original recipe calls for 2 pounds of pasta

    # Calculate the total amount of pasta needed for the reunion
    total_pasta = (reunion_servings / original_recipe_servings) * original_recipe_pasta
    result = total_pasta
    return result

print(solution())