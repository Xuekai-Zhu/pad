def solution():
    """Jim is a maintenance worker at a pool. Every time someone jumps in the pool, they cause 400 ml of water to splash out and evaporate. Jim has to get everyone out of the pool, clean, and refill it when it gets below 80% full. If the pool holds 2000 L of water, how many times can people jump in the pool before Jim has to clean it?"""
    # Define the pool capacity and the amount of water that splashes out each time someone jumps in
    POOL_CAPACITY = 2000
    SPLASH_AMOUNT = 0.4

    # Calculate the maximum number of jumps before the pool needs to be cleaned and refilled
    max_jumps = int((0.8 * POOL_CAPACITY) / SPLASH_AMOUNT)

    # Display the maximum number of jumps
    result = max_jumps
    return result

print(solution())