def solution():
    
    apple_cost_per_dozen = 40
    pear_cost_per_dozen = 50
    num_dozen = 14
    total_apple_cost = apple_cost_per_dozen * num_dozen
    total_pear_cost = pear_cost_per_dozen * num_dozen
    total_cost = total_apple_cost + total_pear_cost
    result = total_cost
    return result

print(solution())