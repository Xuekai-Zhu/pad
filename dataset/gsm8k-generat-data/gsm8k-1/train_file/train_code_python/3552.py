def solution():
    """A swimming pool is being emptied through a drain at the bottom of the pool and filled by a hose at the top. The drain can empty the pool in 4 hours and the hose can fill the pool in 6 hours. The pool holds 120 liters of water. If the pool starts filled with water, how much water will be left after 3 hours?"""
    pool_capacity = 120
    drain_rate = pool_capacity / 4
    fill_rate = pool_capacity / 6
    net_rate = fill_rate - drain_rate
    water_left = pool_capacity - (net_rate * 3)
    result = water_left
    return result

print(solution())