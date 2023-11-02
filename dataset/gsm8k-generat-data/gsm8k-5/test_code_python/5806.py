def solution():
    ice_cubes_in_glass = 8
    ice_cubes_in_pitcher = 2 * ice_cubes_in_glass  # Dylan puts 2 times as many ice cubes in the pitcher as in his glass
    total_ice_cubes = ice_cubes_in_glass + ice_cubes_in_pitcher

    # Calculate number of trays needed to fill all the ice used
    trays_needed = total_ice_cubes // 12 + (total_ice_cubes % 12 > 0)  # Round up to nearest whole tray
    result = trays_needed
    return result

print(solution())