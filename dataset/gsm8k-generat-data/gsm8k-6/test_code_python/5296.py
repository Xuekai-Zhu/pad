def solution():
    muffins_per_day = 12
    cost_per_muffin = 0.75
    selling_price_per_muffin = 1.5

    daily_profit_per_dozen = (selling_price_per_muffin - cost_per_muffin) * muffins_per_day
    weekly_profit = daily_profit_per_dozen * 7

    result = weekly_profit
    return result

print(solution())