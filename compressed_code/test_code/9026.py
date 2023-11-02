def solution():
    
    budget = 60
    shower_gel_price = 4
    tube_of_toothpaste_price = 3
    remaining_budget = 30
    
    
    num_shower_gels = 4
    total_shower_gel_cost = num_shower_gels * shower_gel_price
    
    
    total_toothpaste_cost = tube_of_toothpaste_price
    
    
    total_laundry_detergent_cost = budget - remaining_budget - total_shower_gel_cost - total_toothpaste_cost
    
    result = total_laundry_detergent_cost
    return result

print(solution())