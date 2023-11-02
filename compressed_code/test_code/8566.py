def solution():
    
    
    original_cost = 200
    fuel_increase = 0.2
    new_cost = original_cost * (1 + fuel_increase)
    total_cost = new_cost * 2
    
    result = total_cost
    return result

print(solution())