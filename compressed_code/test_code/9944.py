def solution():
    
    muffins_per_dozen = 12
    daily_cost = muffins_per_dozen * 0.75
    daily_revenue = muffins_per_dozen * 1.5
    daily_profit = daily_revenue - daily_cost
    weekly_profit = daily_profit * 7
    result = weekly_profit
    return result

print(solution())