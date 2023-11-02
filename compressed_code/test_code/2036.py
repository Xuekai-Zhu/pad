def solution():
    
    total_litter_needed = 210/7 * 15  
    num_containers = total_litter_needed / 45  
    total_cost = num_containers * 21  
    result = total_cost
    return result

print(solution())