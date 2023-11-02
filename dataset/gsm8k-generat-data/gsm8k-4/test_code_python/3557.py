def solution():
    """Jim is a maintenance worker at a pool. Every time someone jumps in the pool, they cause 400 ml of water to splash out and evaporate. Jim has to get everyone out of the pool, clean, and refill it when it gets below 80% full. If the pool holds 2000 L of water, how many times can people jump in the pool before Jim has to clean it?"""
    # Define the pool capacity and the amount of water that can be lost before cleaning is needed
    POOL_CAPACITY = 2000
    MIN_WATER_LEVEL = 0.8 * POOL_CAPACITY

    # Define the amount of water lost every time someone jumps in the pool
    WATER_LOSS_PER_JUMP = 0.4

    # Initialize the number of jumps and the current water level
    jumps = 0
    water_level = POOL_CAPACITY

    # Jump into the pool until the water level drops below the minimum level
    while water_level >= MIN_WATER_LEVEL:
        # Increment the number of jumps
        jumps += 1

        # Calculate the amount of water lost
        water_loss = WATER_LOSS_PER_JUMP * 1000

        # Update the water level
        water_level -= water_loss

    # Display the number of jumps before cleaning is needed
    result = jumps
    return result

print(solution())