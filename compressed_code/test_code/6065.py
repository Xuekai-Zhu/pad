def solution():
    
    total_tubs = 9
    cost_of_large_tubs = 6
    total_cost = 48
    cost_of_small_tubs = (total_cost - (cost_of_large_tubs * 3)) / 6
    result = cost_of_small_tubs
    return result

print(solution())