def solution():
    # Calculate the number of servings in 64 fluid ounces for both 8-ounce and 16-ounce servings
    servings_8oz = 64 / 8
    servings_16oz = 64 / 16

    # Calculate the difference in the number of servings
    servings_difference = servings_8oz - servings_16oz
    result = servings_difference
    return result

print(solution())