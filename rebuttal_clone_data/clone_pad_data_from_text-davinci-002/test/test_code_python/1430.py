def solution():
    cost_of_system = 20000
    number_of_zones = 2
    vents_per_zone = 5
    total_vents = number_of_zones * vents_per_zone
    cost_per_vent = cost_of_system / total_vents
    result = cost_per_vent
    return result

print(solution())