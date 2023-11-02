def solution():
    muffins_per_day = 12
    cost_per_muffin = 0.75
    sell_price_per_muffin = 1.5
    days_per_week = 7

    total_cost = muffins_per_day * cost_per_muffin
    total_revenue = muffins_per_day * sell_price_per_muffin
    daily_profit = total_revenue - total_cost
    weekly_profit = daily_profit * days_per_week
    result = weekly_profit
    return result

print(solution())