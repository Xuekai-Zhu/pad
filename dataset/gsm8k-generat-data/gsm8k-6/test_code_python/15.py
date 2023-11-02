def solution():
    # Calculate the cost and revenue of each DVD
    cost_per_DVD = 2000 + 6  # cost of creating the movie + cost of making a DVD
    sales_price_per_DVD = 2.5 * cost_per_DVD  # selling price of a DVD

    # Calculate the profit per DVD and per day
    profit_per_DVD = sales_price_per_DVD - cost_per_DVD
    profit_per_day = profit_per_DVD * 500

    # Calculate the profit per week and per 20 weeks
    profit_per_week = profit_per_day * 5
    total_profit = profit_per_week * 20
    result = total_profit
    return result

print(solution())