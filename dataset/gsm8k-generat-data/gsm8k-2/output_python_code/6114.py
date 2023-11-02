def solution():
    """Pauly is making ice cubes. He needs 10 pounds of cubes. He knows that 2 ounces of water make 1 cube and each cube weighs 1/16th of a pound. It takes him 1 hour to make 10 cubes. Every hour his ice maker run costs $1.50. Every ounce of water costs $0.10. How much will it cost to make all the ice?"""
    water_per_cube = 2
    cube_weight = 1 / 16  # pounds
    total_cube_weight = 10  # pounds
    cubes_needed = total_cube_weight / cube_weight
    water_needed = cubes_needed * water_per_cube
    cost_of_water = water_needed * 0.10
    hours_of_operation = cubes_needed / 10
    cost_of_operation = hours_of_operation * 1.50
    total_cost = cost_of_water + cost_of_operation
    result = total_cost
    return result

print(solution())