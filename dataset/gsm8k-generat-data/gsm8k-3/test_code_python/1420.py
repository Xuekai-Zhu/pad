def solution():
    """Compared to the amount of water she drank, Carla drank three times as much soda minus 6 ounces. If she drank 54 ounces of liquid total, how much water did she drink?"""
    # Define the amount of soda Carla drank in terms of water
    SODA_TO_WATER_RATIO = 3
    SODA_OFFSET = -6

    # Define the total amount of liquid Carla drank
    total_drinks = 54

    # Calculate the amount of water Carla drank
    water_drinks = total_drinks / (SODA_TO_WATER_RATIO + 1)
    water_volume = water_drinks

    # Display the amount of water Carla drank
    result = water_volume
    return result

print(solution())