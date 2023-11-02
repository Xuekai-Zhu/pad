def solution():
    
    price_per_cup = 2
    ingredient_cost = 20
    desired_profit = 80
    cups_needed = (desired_profit + ingredient_cost) / price_per_cup
    result = cups_needed
    return result

print(solution())