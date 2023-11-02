def solution():
    """Pauly is making ice cubes. He needs 10 pounds of cubes. He knows that 2 ounces of water make 1 cube and each cube weighs 1/16th of a pound. It takes him 1 hour to make 10 cubes. Every hour his ice maker run costs $1.50. Every ounce of water costs $0.10. How much will it cost to make all the ice?"""
    cubes_needed = 10
    ounces_per_cube = 2
    pound_per_cube = 1/16
    water_cost_per_ounce = 0.10
    water_ounces_needed = cubes_needed * ounces_per_cube
    water_cost = water_ounces_needed * water_cost_per_ounce
    total_weight = cubes_needed * pound_per_cube
    ice_maker_cost_per_hour = 1.5
    time_to_make_ice = 1
    total_cost = ice_maker_cost_per_hour * time_to_make_ice + water_cost
    
    result = total_cost
    return result

print(solution())