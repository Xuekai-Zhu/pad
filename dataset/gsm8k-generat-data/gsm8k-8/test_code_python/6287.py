def solution():
    # Calculate revenue per tire
    revenue_per_tire = 1.5 * 250

    # Calculate the profit per tire
    profit_per_tire = revenue_per_tire - 250

    # Calculate the profit per day
    profit_per_day = profit_per_tire * 1000

    # Calculate the potential profit per day if able to produce 1200 tires
    potential_profit_per_day = profit_per_tire * 1200

    # Calculate the lost profit per day
    lost_profit_per_day = potential_profit_per_day - profit_per_day

    # Calculate the lost profit per week
    lost_profit_per_week = lost_profit_per_day * 7
    result = lost_profit_per_week
    return result

print(solution())