def solution():
    """Joey needs to take a new prescription. The first day he needs to take one pill. Each day he must take two more pills than the previous day. How many pills will he take in a week?"""
    pills_per_day = 1
    total_pills = 0
    for i in range(7):
        total_pills += pills_per_day
        pills_per_day += 2

    result = total_pills
    return result

print(solution())