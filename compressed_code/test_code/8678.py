def solution():
    
    cheese_weight = 1.5
    meat_weight = 0.5
    cheese_cost_per_kg = 6
    meat_cost_per_kg = 8
    total_cheese_cost = cheese_cost_per_kg * cheese_weight
    total_meat_cost = meat_cost_per_kg * meat_weight
    total_cost = total_cheese_cost + total_meat_cost
    result = total_cost
    return result

print(solution())