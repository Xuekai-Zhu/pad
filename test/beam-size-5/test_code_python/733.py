def solution():
    
    total_cube_size = 32
    giant_cube_size = 4
    medium_cube_size = 2
    small_cube_size = 1/2
    num_giant_cubes = 3
    num_medium_cubes = 7
    num_small_cubes = 8
    total_giant_water = giant_cube_size * num_giant_cubes
    total_medium_water = medium_cube_size * num_medium_cubes
    total_small_water = small_cube_size * num_small_cubes
    total_water = total_giant_water + total_medium_water + total_small_water
    water_left = total_cube_size - total_water
    result = water_left
    return result

print(solution())