def solution():
    """A farmer has 52 cows. Each cow gives 5 liters of milk a day. How many liters of milk does the farmer get in a week?"""
    cows = 52
    liters_per_cow_per_day = 5
    days_per_week = 7
    total_liters = cows * liters_per_cow_per_day * days_per_week
    result = total_liters
    return result

print(solution())