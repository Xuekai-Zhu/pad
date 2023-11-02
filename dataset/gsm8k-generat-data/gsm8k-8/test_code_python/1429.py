def solution():
    # Define the initial investment and profit margin
    initial_investment = 3000
    profit_margin = 1/3

    # Calculate the total profit
    total_profit = initial_investment * profit_margin

    # Calculate the total cost of the 200 units
    total_cost = initial_investment + total_profit

    # Calculate the cost per unit
    cost_per_unit = total_cost / 200

    # Calculate the selling price including the profit margin
    selling_price = cost_per_unit / (1 - profit_margin)
    result = selling_price
    return result

print(solution())