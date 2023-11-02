def solution():
    mountain_dew = 6 * 12  # Carrie adds 6 cans, each containing 12 oz of Mountain Dew
    ice = 28  # Carrie adds 28 oz of ice
    fruit_juice = 40  # Carrie adds a 40 oz bottle of fruit juice

    # Calculate the total volume of punch
    total_volume = mountain_dew + ice + fruit_juice

    # Calculate the number of 10 oz servings of punch
    servings = total_volume / 10

    result = servings
    return result

print(solution())