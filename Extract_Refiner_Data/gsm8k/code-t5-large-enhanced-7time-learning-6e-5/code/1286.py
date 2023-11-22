def solution():
    
    # Define the number of sunflower seeds in a dozen
    SUNFLOWER_SEEDS_PER_DOZEN = 12

    # Define the number of seeds in a small sunflower
    SMALL_SEEDS = 3 * SUNFLOWER_SEEDS_PER_DOZEN

    # Define the number of seeds in a large sunflower
    LARGE_SEEDS = SMALL_SEEDS * 1.5

    # Calculate the total number of sunflower seeds
    total_seeds = SMALL_SEEDS + LARGE_SEEDS

    # Display the total number of sunflower seeds
    result = total_seeds
    return result

print(solution())