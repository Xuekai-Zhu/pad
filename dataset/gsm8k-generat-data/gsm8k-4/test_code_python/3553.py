def solution():
    """A swimming pool is being emptied through a drain at the bottom of the pool and filled by a hose at the top. The drain can empty the pool in 4 hours and the hose can fill the pool in 6 hours. The pool holds 120 liters of water. If the pool starts filled with water, how much water will be left after 3 hours?"""
    # Define the rate of the drain and the hose
    drain_rate = 1 / 4
    hose_rate = 1 / 6

    # Define the total capacity of the pool
    pool_capacity = 120

    # Calculate the combined rate of filling and draining
    net_rate = hose_rate - drain_rate

    # Calculate the amount of water left after 3 hours
    water_left = pool_capacity - (3 * net_rate * pool_capacity)

    # Return the result
    result = water_left
    return result

print(solution())