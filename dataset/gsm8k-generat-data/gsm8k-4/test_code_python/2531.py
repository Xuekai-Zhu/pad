def solution():
    """The cost of Joe's new HVAC system is $20,000. It includes 2 conditioning zones, each with 5 vents. In dollars, what is the cost of the system per vent?"""
    # Define the cost of the HVAC system and the number of vents
    hvac_cost = 20000
    num_zones = 2
    num_vents_per_zone = 5

    # Calculate the total number of vents
    total_vents = num_zones * num_vents_per_zone

    # Calculate the cost per vent
    cost_per_vent = hvac_cost / total_vents

    # Return the result
    result = cost_per_vent
    return result

print(solution())