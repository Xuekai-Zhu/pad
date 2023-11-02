def solution():
    """There are four growing trees. The first tree grows 1 meter/day, the second grows the same amount in half the time, the third grows 2 meters/day, and the fourth tree grows a meter more than the third each day. How many meters did the trees grow in total in 4 days?"""
    growth_rates = [1, 2, 2, 3]  # meters per day
    total_growth = 0

    for i in range(4):
        if i == 1:
            growth_rates[i] = growth_rates[0] * 2
        if i == 3:
            growth_rates[i] = growth_rates[2] + 1

        total_growth += growth_rates[i] * 4

    result = total_growth
    return result

print(solution())