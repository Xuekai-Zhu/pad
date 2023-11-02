def solution():
    ice_cubes_in_glass = 8
    ice_cubes_in_pitcher = ice_cubes_in_glass * 2
    spaces_in_ice_cube_tray = 12
    ice_cube_trays_needed = ice_cubes_in_pitcher / spaces_in_ice_cube_tray
    result = ice_cube_trays_needed
    return result

print(solution())