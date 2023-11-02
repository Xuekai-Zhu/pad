def solution():
    # Define the cost and selling price of one chocolate bar
    cost_per_bar = 5 + 2
    selling_price_per_bar = 90 / 5

    # Calculate the profit per bar
    profit_per_bar = selling_price_per_bar - cost_per_bar

    # Calculate the total profit for all five bars
    total_profit = profit_per_bar * 5
    result = total_profit
    return result

print(solution())