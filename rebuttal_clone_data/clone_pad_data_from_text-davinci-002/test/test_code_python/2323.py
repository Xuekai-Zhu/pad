def solution():
    chickens_bought = 3
    cost_per_chicken = 3
    total_cost = chickens_bought * cost_per_chicken
    potatoes_cost = 15 - total_cost
    result = potatoes_cost
    return result

print(solution())