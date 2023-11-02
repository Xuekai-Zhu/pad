def solution():
    """The cost of Joe's new HVAC system is $20,000. It includes 2 conditioning zones, each with 5 vents. In dollars, what is the cost of the system per vent?"""
    cost_of_system = 20000
    num_zones = 2
    num_vents_per_zone = 5
    total_num_vents = num_zones * num_vents_per_zone
    cost_per_vent = cost_of_system / total_num_vents
    result = cost_per_vent
    return result

print(solution())