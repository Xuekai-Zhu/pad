def solution():
    
    cost_of_system = 20000
    num_zones = 2
    num_vents_per_zone = 5
    total_num_vents = num_zones * num_vents_per_zone
    cost_per_vent = cost_of_system / total_num_vents
    result = cost_per_vent
    return result

print(solution())