def solution():
    """Each dandelion produces 300 seeds. 1/3rd of the seeds land in water and die. 1/6 of the starting number are eaten by insects. Half the remainder sprout and are immediately eaten. How many dandelions survive long enough to flower?"""
    # Define the number of seeds produced by each dandelion
    SEEDS_PER_DANDELION = 300

    # Calculate the number of seeds that land in water and die
    dead_seeds = SEEDS_PER_DANDELION / 3

    # Calculate the number of seeds that are eaten by insects
    eaten_seeds = SEEDS_PER_DANDELION / 6

    # Calculate the number of seeds that sprout and are immediately eaten
    sprouted_seeds = (SEEDS_PER_DANDELION - dead_seeds - eaten_seeds) / 2

    # Calculate the number of dandelions that survive long enough to flower
    remaining_seeds = SEEDS_PER_DANDELION - dead_seeds - eaten_seeds - sprouted_seeds
    surviving_dandelions = remaining_seeds / SEEDS_PER_DANDELION

    # Display the number of surviving dandelions
    result = surviving_dandelions
    return result

print(solution())