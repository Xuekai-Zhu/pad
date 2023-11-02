def solution():
    """Phoebe eats 1 serving and gives her dog 1 serving of peanut butter for a bedtime snack. Each jar of peanut butter has 15 servings.  How many jars will she need to make sure she and her dog have enough to last for 30 days?"""
    # Define the number of servings per day
    servings_per_day = 2

    # Define the number of days to plan for
    days = 30

    # Calculate the total number of servings needed 
    total_servings = servings_per_day * days

    # Calculate the number of jars needed to have enough servings
    jars_needed = total_servings / 15

    # Round up to the nearest whole jar
    jars_needed = math.ceil(jars_needed)

    # Return the result
    result = jars_needed
    return result

print(solution())