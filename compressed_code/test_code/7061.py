def solution():
    
    
    first_pair_cost = 40
    second_pair_cost = 60
    original_cost = first_pair_cost + second_pair_cost
    
    
    if first_pair_cost <= second_pair_cost:
        discounted_pair_cost = first_pair_cost * 0.5
        undiscounted_pair_cost = second_pair_cost
    else:
        discounted_pair_cost = second_pair_cost * 0.5
        undiscounted_pair_cost = first_pair_cost
    
    
    total_discounted_cost = undiscounted_pair_cost + discounted_pair_cost
    final_cost = total_discounted_cost - (total_discounted_cost * 0.25)
    
    result = final_cost
    return result

print(solution())