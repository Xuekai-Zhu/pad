def solution():
    # Calculate the number of servings Simeon used to drink in a day
    servings_old = 64 / 8  # Simeon used to drink 8-ounce servings

    # Calculate the number of servings Simeon now drinks in a day
    servings_new = 64 / 16  # Simeon now drinks 16-ounce servings

    # Calculate the difference in the number of servings
    servings_difference = servings_old - servings_new

    result = servings_difference
    return result

print(solution())