def solution():
    target_weight = 10  # pounds
    cubes_per_pound = 16
    water_per_cube = 2/16  # pounds
    cubes_per_hour = 10
    hourly_cost = 1.5
    cost_per_ounce_of_water = 0.1/16  # pounds

    # Calculate the total number of cubes needed
    total_cubes = target_weight * cubes_per_pound

    # Calculate the total weight of water needed
    water_weight = total_cubes * water_per_cube

    # Calculate the cost of the water
    water_cost = water_weight * cost_per_ounce_of_water

    # Calculate the total cost of making all the ice, including the hourly cost of the ice maker
    total_cost = water_cost + (hourly_cost * (total_cubes / cubes_per_hour))
    result = total_cost
    return result

print(solution())