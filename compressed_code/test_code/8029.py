def solution():
    
    beef_pounds = 100
    beef_per_taco = 0.25
    tacos_made = beef_pounds / beef_per_taco
    taco_sale_price = 2
    taco_cost = 1.5
    profit_per_taco = taco_sale_price - taco_cost
    total_profit = tacos_made * profit_per_taco
    result = total_profit
    return result

print(solution())