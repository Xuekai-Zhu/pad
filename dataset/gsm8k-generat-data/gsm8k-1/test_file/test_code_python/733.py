def solution():
    """Peter wants to make different sized ice cubes with 32 ounces of water. He can make giant cubes that use 4 ounces per cube, medium cubes that use 2 ounces, and small cubes that use 1/2 an ounce. If he makes 3 giant cubes, 7 medium cubes, and 8 small cubes, how many ounces of water does he have left?"""
    water_used_by_giant_cubes = 3 * 4
    water_used_by_medium_cubes = 7 * 2
    water_used_by_small_cubes = 8 * 0.5

    total_water_used = water_used_by_giant_cubes + water_used_by_medium_cubes + water_used_by_small_cubes
    water_left = 32 - total_water_used
    result = water_left
    return result

print(solution())