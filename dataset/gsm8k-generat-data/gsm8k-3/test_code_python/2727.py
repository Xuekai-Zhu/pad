def solution():
    """Oshea bought 200 basil seeds. He wants to plant them in planters. He has 4 large planters that can hold 20 seeds each. He also has small planters that can hold 4 seeds each. How many small planters will he need to plant all the basil seeds?"""
    # Define the number of seeds and planter capacities
    SEEDS = 200
    LARGE_PLANTER_CAPACITY = 20
    SMALL_PLANTER_CAPACITY = 4

    # Calculate the number of large planters needed
    large_planters = SEEDS // LARGE_PLANTER_CAPACITY
    seeds_remaining = SEEDS % LARGE_PLANTER_CAPACITY

    # Calculate the number of small planters needed
    small_planters = seeds_remaining // SMALL_PLANTER_CAPACITY
    if seeds_remaining % SMALL_PLANTER_CAPACITY != 0:
        # Need one more small planter if there are any remaining seeds
        small_planters += 1

    # Calculate the total number of planters needed
    total_planters = large_planters + small_planters

    # Display the total number of small planters needed
    result = small_planters
    return result

print(solution())