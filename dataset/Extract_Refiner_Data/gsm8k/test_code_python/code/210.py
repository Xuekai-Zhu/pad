def solution():
    
    # Define the leak rate of the pool
    leak_rate = 4  # gallons/minute

    # Calculate the total amount of water in the pool
    total_water = 0

    # Calculate the amount of water in the pool 4 minutes ago
    pool_4_min = 2 * (4 * leak_rate)

    # Calculate the amount of water in the pool now
    pool_now = pool_4_min * leak_rate

    # Display the amount of water in the pool now
    result = pool_now
    return result

print(solution())