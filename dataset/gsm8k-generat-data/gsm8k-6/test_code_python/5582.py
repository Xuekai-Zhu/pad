def solution():
    # Calculate the total height of the first 100 floors
    height_first_100_floors = 100 * 16.5

    # Calculate the height of the 101st floor by subtracting the total height of the first 100 floors from the total height of Taipei 101
    height_101st_floor = 1673 - height_first_100_floors
    result = height_101st_floor
    return result

print(solution())