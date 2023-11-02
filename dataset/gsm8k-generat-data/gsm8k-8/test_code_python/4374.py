def solution():
    # Calculate the total number of servings Phoebe and her dog need per day
    servings_per_day = 2

    # Calculate the total number of servings Phoebe and her dog need for 30 days
    servings_per_month = servings_per_day * 30

    # Calculate the number of jars needed to have enough servings for 30 days
    jars_needed = servings_per_month / 15
    result = jars_needed
    return result

print(solution())