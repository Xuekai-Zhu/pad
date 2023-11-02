def solution():
    floors = 100  # Taipei 101 has 101 floors, but we are only interested in the first 100 floors
    height_per_floor = 16.5  # The height of each floor from the first to the 100th floor, in feet
    total_height = floors * height_per_floor  # The total height of the first to 100th floors, in feet
    height_101st_floor = 1673 - total_height  # The height of the 101st floor, in feet

    result = height_101st_floor
    return result

print(solution())