def solution():
    units = 200  # Ronald bought 200 units
    initial_investment = 3000  # Ronald invested $3000 to buy the units
    profit_margin = 1/3  # Ronald wants to gain 1/3 of the initial investment in profits

    # Calculate the total profit
    total_profit = initial_investment * profit_margin

    # Calculate the total revenue needed to cover the initial investment and profits
    total_revenue = initial_investment + total_profit

    # Calculate the selling price per unit
    selling_price_per_unit = total_revenue / units
    result = selling_price_per_unit
    return result

print(solution())