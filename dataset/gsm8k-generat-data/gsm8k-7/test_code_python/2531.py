def solution():
    system_cost = 20000
    num_zones = 2
    num_vents_per_zone = 5

    # Calculate the total number of vents in the system
    total_num_vents = num_zones * num_vents_per_zone

    # Calculate the cost per vent
    cost_per_vent = system_cost / total_num_vents
    result = cost_per_vent
    return result

print(solution())