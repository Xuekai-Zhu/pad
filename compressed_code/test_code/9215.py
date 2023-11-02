def solution():
    
    num_ducks = 30
    cost_per_duck = 10
    weight_per_duck = 4
    price_per_pound = 5
    total_cost = num_ducks * cost_per_duck
    total_weight = num_ducks * weight_per_duck
    total_sale_price = total_weight * price_per_pound
    profit = total_sale_price - total_cost
    result = profit
    return result

print(solution())