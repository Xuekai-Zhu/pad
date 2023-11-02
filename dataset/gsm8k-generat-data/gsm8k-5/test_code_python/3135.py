def solution():
    # Calculate the volume of the pool in cubic feet
    pool_volume = 10 * 6 * 20

    # Convert the volume to liters
    pool_volume_liters = pool_volume * 25

    # Calculate the cost of filling the pool with water
    water_cost = pool_volume_liters * 3

    result = water_cost
    return result

print(solution())