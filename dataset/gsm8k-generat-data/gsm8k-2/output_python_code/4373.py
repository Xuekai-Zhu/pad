def solution():
    """Phoebe eats 1 serving and gives her dog 1 serving of peanut butter for a bedtime snack. Each jar of peanut butter has 15 servings.
    How many jars will she need to make sure she and her dog have enough to last for 30 days?"""
    servings_per_day = 2
    days = 30
    jars_per_day = servings_per_day / 15
    total_jars = jars_per_day * days
    result = total_jars
    return result

print(solution())