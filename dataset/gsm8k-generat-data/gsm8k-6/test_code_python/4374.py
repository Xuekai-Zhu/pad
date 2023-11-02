def solution():
    # Calculate the total number of servings of peanut butter needed for Phoebe and her dog for 30 days
    servings_per_day = 2  # Phoebe eats 1 serving and gives her dog 1 serving
    total_servings = servings_per_day * 30  # assuming 30 days in a month
    servings_per_jar = 15  # each jar of peanut butter has 15 servings
    jars_needed = total_servings // servings_per_jar + 1  # round up to the nearest jar
    result = jars_needed
    return result

print(solution())