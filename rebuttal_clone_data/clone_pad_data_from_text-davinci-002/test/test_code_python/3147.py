def solution():
    total_height = 1673
    floors = 101
    height_first_100_floors = 16.5 * 100
    height_101st_floor = total_height - height_first_100_floors
    result = height_101st_floor
    return result

print(solution())