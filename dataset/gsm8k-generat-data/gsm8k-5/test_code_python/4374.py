def solution():
    servings_per_day = 2  # Phoebe and her dog each get 1 serving of peanut butter per day
    servings_per_jar = 15  # Each jar of peanut butter has 15 servings
    days = 30  # Phoebe wants to have enough peanut butter for 30 days

    # Calculate the total number of servings needed for 30 days
    total_servings = servings_per_day * days

    # Calculate the total number of jars needed for 30 days
    jars_needed = (total_servings // servings_per_jar) + 1  # Round up to the nearest jar
    result = jars_needed
    return result

print(solution())