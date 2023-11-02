def solution():
    """A one-way ticket costs $2. A 30-day pass costs $50. What's the minimum number of rides you will need to take every month so that the 30-day pass is strictly cheaper per ride?"""
    one_way_cost = 2
    pass_cost = 50
    rides_per_month = 0
    while (rides_per_month + 1) * one_way_cost < pass_cost:
        rides_per_month += 1
    result = rides_per_month + 1
    return result

print(solution())