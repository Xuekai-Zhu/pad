def solution():
    """Phoebe eats 1 serving and gives her dog 1 serving of peanut butter for a bedtime snack. Each jar of peanut butter has 15 servings. How many jars will she need to make sure she and her dog have enough to last for 30 days?"""
    servings_per_day = 2
    servings_per_jar = 15
    days = 30
    total_servings_needed = servings_per_day * days
    jars_needed = total_servings_needed / servings_per_jar
    result = jars_needed
    return result

print(solution())