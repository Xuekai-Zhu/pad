def solution():
    """Taipei 101 in Taiwan is 1,673 feet tall with 101 floors. Suppose the first to 100th floors have height each equal to 16.5 feet, how high is the 101st floor?"""
    # Define the height of the first 100 floors
    first_100_floors = 100 * 16.5

    # Calculate the height of the 101st floor
    height_101st_floor = 1673 - first_100_floors

    # Return the result
    result = height_101st_floor
    return result

print(solution())