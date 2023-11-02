def solution():
    
    bottle_cost = 30.00
    servings_per_bottle = 16
    serving_price = 8.00
    revenue_per_bottle = servings_per_bottle * serving_price
    profit_per_bottle = revenue_per_bottle - bottle_cost
    result = profit_per_bottle
    return result

print(solution())