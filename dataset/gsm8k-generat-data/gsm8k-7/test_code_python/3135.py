def solution():
    # Calculate the volume of the pool in cubic feet
    pool_volume = 10 * 6 * 20

    # Calculate the volume of the pool in liters
    pool_volume_liters = pool_volume * 25

    # Calculate the cost to fill the pool
    cost = pool_volume_liters * 3

    result = cost
    return result

print(solution())