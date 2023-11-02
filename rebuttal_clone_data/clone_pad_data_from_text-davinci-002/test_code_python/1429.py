def solution():
    initial_investment = 3000
    units_bought = 200
    desired_profit = initial_investment / 3
    selling_price = desired_profit + initial_investment
    price_per_unit = selling_price / units_bought
    result = price_per_unit
    
    return result

print(solution())