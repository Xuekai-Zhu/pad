def solution():
    # Convert the required amount of soy sauce for each recipe to ounces
    recipe1_soy_sauce = 2 * 8  # 2 cups = 16 ounces
    recipe2_soy_sauce = 1 * 8  # 1 cup = 8 ounces
    recipe3_soy_sauce = 3 * 8  # 3 cups = 24 ounces

    # Calculate the total amount of soy sauce required
    total_soy_sauce = recipe1_soy_sauce + recipe2_soy_sauce + recipe3_soy_sauce

    # Calculate the number of bottles of soy sauce required
    bottles_of_soy_sauce = total_soy_sauce // 16 + 1  # Round up to the nearest whole bottle

    result = bottles_of_soy_sauce
    return result

print(solution())