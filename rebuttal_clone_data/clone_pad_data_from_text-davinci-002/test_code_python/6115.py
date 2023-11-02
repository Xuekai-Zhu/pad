def solution():
    pounds_of_ice = 10
    ounces_per_cube = 2
    cubes_per_pound = 16
    total_cubes = pounds_of_ice * cubes_per_pound
    total_ounces = total_cubes * ounces_per_cube
    cost_per_hour = 1.50
    cost_per_ounce = 0.10
    total_cost = cost_per_hour + (total_ounces * cost_per_ounce)
    result = total_cost
    return result

print(solution())