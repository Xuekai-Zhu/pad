def solution():
    
    max_load = 900  
    lemon_bag_weight = 8  
    num_bags = 100  
    total_weight = num_bags * lemon_bag_weight  
    remaining_capacity = max_load - total_weight  
    result = remaining_capacity
    return result

print(solution())