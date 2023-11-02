def solution():
    elevation_increase = 1450 - 100  # John's elevation increases by 1350 feet
    vertical_distance_traveled = 1 * elevation_increase  # John travels 1 foot vertically for every 2 feet horizontally
    horizontal_distance_traveled = 2 * vertical_distance_traveled  # John travels 2 feet horizontally for every 1 foot vertically

    result = horizontal_distance_traveled
    return result

print(solution())