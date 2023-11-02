def solution():
    
    water_per_cube = 2
    cube_weight = 1 / 16  
    total_cube_weight = 10  
    cubes_needed = total_cube_weight / cube_weight
    water_needed = cubes_needed * water_per_cube
    cost_of_water = water_needed * 0.10
    hours_of_operation = cubes_needed / 10
    cost_of_operation = hours_of_operation * 1.50
    total_cost = cost_of_water + cost_of_operation
    result = total_cost
    return result

print(solution())