def solution():
    # Calculate the volume of the pool
    pool_volume = 10 * 10 * 6

    # Calculate the number of gallons needed to fill the pool
    pool_gallons = pool_volume * 7.48

    # Calculate the total gallons used by Jerry for non-pool purposes
    non_pool_gallons = 100

    # Calculate the remaining gallons Jerry can use for showers
    shower_gallons = 1000 - pool_gallons - non_pool_gallons

    # Calculate the maximum number of showers Jerry can take
    max_showers = shower_gallons // 20

    result = max_showers
    return result

print(solution())