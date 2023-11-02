def solution():
    tires_produced = 1000  # John can produce 1000 tires a day
    cost_per_tire = 250  # It costs $250 to produce each tire
    selling_price = 1.5 * cost_per_tire  # John sells each tire for 1.5 times the production cost
    tires_sold = 1200  # John could sell 1200 tires a day if his factory produced more

    # Calculate John's daily profit
    profit_per_tire = selling_price - cost_per_tire
    daily_profit = profit_per_tire * tires_sold

    # Calculate John's weekly profit
    weekly_profit = daily_profit * 7

    # Calculate the potential profit John would lose out on if he could produce and sell all 1200 tires a day
    potential_daily_profit = profit_per_tire * (1200 - tires_produced)
    potential_weekly_profit = potential_daily_profit * 7
    lost_profit = potential_weekly_profit - weekly_profit

    result = lost_profit
    return result

print(solution())