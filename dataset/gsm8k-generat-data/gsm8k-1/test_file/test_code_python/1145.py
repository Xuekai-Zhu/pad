def solution():
    """Jen got 3 fish. They each need $1 worth of food a day. How much does she spend on food in the month of May?"""
    fish_count = 3
    cost_per_fish_per_day = 1
    days_in_May = 31
    total_cost = fish_count * cost_per_fish_per_day * days_in_May
    result = total_cost
    return result

print(solution())