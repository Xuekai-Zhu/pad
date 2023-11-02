def solution():
    """The cost of Joe's new HVAC system is $20,000.  It includes 2 conditioning zones, each with 5 vents.  In dollars, what is the cost of the system per vent?"""
    # Define the total cost of the HVAC system
    total_cost = 20000

    # Define the number of conditioning zones and vents per zone
    num_zones = 2
    num_vents_per_zone = 5

    # Calculate the total number of vents in the system
    total_num_vents = num_zones * num_vents_per_zone

    # Calculate the cost per vent
    cost_per_vent = total_cost / total_num_vents

    # Display the cost per vent
    result = cost_per_vent
    return result

print(solution())