def solution():
    num_ice_cubes_glass = 8
    num_ice_cubes_pitcher = 2*num_ice_cubes_glass
    num_ice_cubes_total = num_ice_cubes_glass + num_ice_cubes_pitcher
    num_ice_cube_trays = num_ice_cubes_total / 12
    num_ice_cube_trays = int(num_ice_cube_trays)

    # Round up if there are any remaining ice cubes
    if num_ice_cubes_total % 12 != 0:
        num_ice_cube_trays += 1

    result = num_ice_cube_trays
    return result

print(solution())