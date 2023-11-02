def solution():
    num_units = 200
    initial_investment = 3000
    profit_margin = 1/3

    # Calculate the total profit that Ronald wants to make
    total_profit = initial_investment * profit_margin

    # Calculate the total cost of each unit, including the profit margin
    cost_per_unit = (initial_investment + total_profit) / num_units

    result = cost_per_unit
    return result

print(solution())