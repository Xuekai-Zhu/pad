def solution():
    """Taipei 101 in Taiwan is 1,673 feet tall with 101 floors. Suppose the first to 100th floors have height each equal to 16.5 feet, how high is the 101st floor?"""
    floor_height = 16.5
    total_height = (floor_height * 100)
    height_101st_floor = 1673 - total_height
    result = height_101st_floor
    return result

print(solution())