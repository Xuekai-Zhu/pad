def solution():
    daily_rate = 30
    weekly_rate = 190
    days = 11
    if days >= 7:
        total_cost = weekly_rate
    else:
        total_cost = daily_rate * days
    result = total_cost
    return result

print(solution())