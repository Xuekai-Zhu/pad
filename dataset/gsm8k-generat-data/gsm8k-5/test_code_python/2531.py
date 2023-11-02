def solution():
    system_cost = 20000  # The cost of Joe's HVAC system is $20,000
    num_zones = 2  # The system includes 2 conditioning zones
    num_vents_per_zone = 5  # Each zone has 5 vents

    # Calculate the total number of vents in the system
    total_vents = num_zones * num_vents_per_zone

    # Calculate the cost per vent
    cost_per_vent = system_cost / total_vents
    result = cost_per_vent
    return result

print(solution())