def solution():
    muffins_per_dozen = 12
    cost_per_muffin = 0.75
    selling_price_per_muffin = 1.5
    days_per_week = 7

    # Calculate the total cost of a dozen muffins
    cost_per_dozen = muffins_per_dozen * cost_per_muffin

    # Calculate the profit per dozen muffins
    profit_per_dozen = (selling_price_per_muffin - cost_per_muffin) * muffins_per_dozen

    # Calculate the profit per day
    profit_per_day = profit_per_dozen * (1/days_per_week)

    # Calculate the weekly profit
    weekly_profit = profit_per_day * days_per_week
    result = weekly_profit
    return result

print(solution())