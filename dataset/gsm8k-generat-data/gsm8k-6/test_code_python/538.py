def solution():
    # Calculate the reseller's selling price with a 15% profit
    cost_price = 3000
    profit_percent = 15
    selling_price = cost_price * (1 + profit_percent/100)
    result = selling_price
    return result

print(solution())