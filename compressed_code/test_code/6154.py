def solution():
    
    original_cost = 500
    increased_cost = original_cost + (2/5)*original_cost
    discounted_cost = increased_cost - 0.15*increased_cost
    money_needed = discounted_cost - original_cost
    result = money_needed
    return result

print(solution())