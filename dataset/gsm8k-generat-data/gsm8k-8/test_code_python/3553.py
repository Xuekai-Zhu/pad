def solution():
    pool_volume = 120
    drain_rate = pool_volume / 4
    hose_rate = pool_volume / 6

    # After 3 hours, 3/4 of the water will be drained out and 1/2 of the water will be filled up
    water_left = (pool_volume - (3/4 * pool_volume)) + (1/2 * (3/6 * pool_volume))
    result = water_left
    return result

print(solution())