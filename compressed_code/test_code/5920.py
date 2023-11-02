def solution():
    
    
    
    pansies_cost = 5 * 2.5
    hydrangea_cost = 12.5
    petunias_cost = 5 * 1
    total_cost = pansies_cost + hydrangea_cost + petunias_cost
    
    
    discount = total_cost * 0.1
    total_cost_discounted = total_cost - discount
    
    
    change = 50 - total_cost_discounted
    result = change
    
    return result

print(solution())