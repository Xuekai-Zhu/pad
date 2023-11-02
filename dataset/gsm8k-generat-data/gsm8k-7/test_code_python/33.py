def solution():
    water_cups = 10
    flour_cups = 16
    salt_teaspoons = 0.5 * flour_cups

    # Calculate the total amount of ingredients needed
    total_water_flour = water_cups + flour_cups
    total_salt = salt_teaspoons / 3  # 1 teaspoon = 1/3 tablespoon

    # Add up all the ingredients
    total = total_water_flour + total_salt
    result = total
    return result

print(solution())