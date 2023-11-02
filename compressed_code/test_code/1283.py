def solution():
    
    budget = 3000
    food_cost = budget / 3
    supplies_cost = budget / 4
    wage_cost = budget - food_cost - supplies_cost
    result = wage_cost
    return result

print(solution())