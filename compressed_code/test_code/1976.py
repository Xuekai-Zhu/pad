def solution():
    
    system_cost = 20000
    num_zones = 2
    num_vents = 5
    total_vents = num_zones * num_vents
    cost_per_vent = system_cost / total_vents
    result = cost_per_vent
    return result

print(solution())