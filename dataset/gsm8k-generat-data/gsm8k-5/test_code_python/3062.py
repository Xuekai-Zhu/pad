def solution():
    vegetables_per_serving = 1  # Each serving has 1 cup of vegetables
    broth_per_serving = 2.5  # Each serving has 2.5 cups of broth
    servings = 8  # We need to calculate the total amount needed for 8 servings

    # Calculate the total amount of vegetables needed for 8 servings
    total_vegetables = vegetables_per_serving * servings

    # Calculate the total amount of broth needed for 8 servings
    total_broth = broth_per_serving * servings

    # Combine the total amounts of vegetables and broth
    total_combined = total_vegetables + total_broth

    # Convert the total combined amount to pints
    pints = total_combined / 2
    result = pints
    return result

print(solution())