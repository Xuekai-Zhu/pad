def solution():
    # Calculate the total cups of vegetables and broth needed for 8 servings
    total_veggies = 1 * 8  # 1 cup of veggies per serving
    total_broth = 2.5 * 8  # 2.5 cups of broth per serving
    total_cups = total_veggies + total_broth  # total cups of veggies and broth

    # Convert total cups to pints (1 pint = 2 cups)
    total_pints = total_cups / 2

    result = total_pints
    return result

print(solution())