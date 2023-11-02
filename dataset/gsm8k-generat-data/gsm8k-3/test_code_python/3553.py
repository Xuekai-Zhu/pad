def solution():
    """A swimming pool is being emptied through a drain at the bottom of the pool and filled by a hose at the top. The drain can empty the pool in 4 hours and the hose can fill the pool in 6 hours. The pool holds 120 liters of water. If the pool starts filled with water, how much water will be left after 3 hours?"""
    # Define the rate of the drain and hose
    DRAIN_RATE = 1 / 4
    HOSE_RATE = 1 / 6

    # Define the volume of the pool
    POOL_VOLUME = 120

    # Calculate the rate of change in water level
    rate = HOSE_RATE - DRAIN_RATE

    # Calculate the amount of water remaining after 3 hours
    remaining_volume = POOL_VOLUME + rate * 3

    # Display the remaining amount of water
    result = remaining_volume
    return result

print(solution())