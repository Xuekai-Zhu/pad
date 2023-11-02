def solution():
    """The cost of Joe's new HVAC system is $20,000. It includes 2 conditioning zones, each with 5 vents. In dollars, what is the cost of the system per vent?"""
    system_cost = 20000
    num_zones = 2
    num_vents = 5
    total_vents = num_zones * num_vents
    cost_per_vent = system_cost / total_vents
    result = cost_per_vent
    return result

print(solution())