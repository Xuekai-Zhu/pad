def solution():
    
    singers = 30
    current_robes = 12
    needed_robes = singers - current_robes
    cost_per_robe = 2
    total_cost = needed_robes * cost_per_robe
    result = total_cost
    
    return result

print(solution())