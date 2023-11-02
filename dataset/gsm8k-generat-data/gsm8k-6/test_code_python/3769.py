def solution():
    # Calculate the total area of fabric used for each type of flag
    area_square = 16 * (4**2)
    area_wide = 20 * (5*3)
    area_tall = 10 * (3*5)

    # Calculate the total area of fabric used
    total_area_used = area_square + area_wide + area_tall

    # Calculate the remaining fabric
    remaining_fabric = 1000 - total_area_used
    result = remaining_fabric
    return result

print(solution())