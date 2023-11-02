def solution():
    """Bob orders a dozen muffins a day for $0.75 each and sells them for $1.5 each. How much profit does he make a week?"""
    muffins_per_dozen = 12
    daily_cost = muffins_per_dozen * 0.75
    daily_revenue = muffins_per_dozen * 1.5
    daily_profit = daily_revenue - daily_cost
    weekly_profit = daily_profit * 7
    result = weekly_profit
    return result

print(solution())