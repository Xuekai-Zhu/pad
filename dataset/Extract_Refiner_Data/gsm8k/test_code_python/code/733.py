def solution():
    
    # Define the amount of water used for each cube size
    GIANT_CUBE_SIZE = 4
    MEDIUM_CUBE_SIZE = 2
    SMALL_CUBE_SIZE = 0.5

    # Define the number of each cube Peter makes
    giant_cubes = 3
    medium_cubes = 7
    small_cubes = 8

    # Calculate the total amount of water used
    total_water_used = (giant_cubes * GIANT_CUBE_SIZE) + (medium_cubes * MEDIUM_CUBE_SIZE) + (small_cubes * SMALL_CUBE_SIZE)

    # Calculate the amount of water left
    water_left = 32 - total_water_used

    # Display the amount of water left
    result = water_left
    return result

print(solution())