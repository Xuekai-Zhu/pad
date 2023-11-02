def solution():
    """Tom rents a helicopter for 2 hours a day for 3 days. It cost $75 an hour to rent. How much did he pay?"""
    hours_per_day = 2
    days = 3
    cost_per_hour = 75
    total_cost = hours_per_day * cost_per_hour * days
    result = total_cost
    return result

print(solution())