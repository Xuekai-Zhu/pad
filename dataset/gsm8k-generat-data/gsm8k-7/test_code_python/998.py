def solution():
    pool_capacity = 60
    hose_rate = 1.6
    leak_rate = 0.1

    # Calculate the effective filling rate of the pool
    filling_rate = hose_rate - leak_rate

    # Calculate the time it will take to fill the pool
    time_to_fill = pool_capacity / filling_rate
    result = time_to_fill
    return result

print(solution())