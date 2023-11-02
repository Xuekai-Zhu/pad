def solution():
    # Calculate the profit Ronald wants to make on each phone
    initial_investment = 3000  # cost of buying 200 units
    profit_margin = 1/3 * initial_investment / 200
    # Calculate the selling price for each phone, including the profit margin
    selling_price = (initial_investment/200) + profit_margin
    result = selling_price
    return result

print(solution())