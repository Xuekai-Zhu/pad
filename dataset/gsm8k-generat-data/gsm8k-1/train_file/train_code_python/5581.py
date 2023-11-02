def solution():
    """Taipei 101 in Taiwan is 1,673 feet tall with 101 floors. Suppose the first to 100th floors have height each equal to 16.5 feet, how high is the 101st floor?"""
    total_height = 1673
    floors = 101
    height_per_floor = 16.5
    height_100_floors = (floors - 1) * height_per_floor
    height_101_floor = total_height - height_100_floors
    result = height_101_floor
    return result

print(solution())