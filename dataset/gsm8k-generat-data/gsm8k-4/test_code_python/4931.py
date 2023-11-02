def solution():
    """Each dandelion produces 300 seeds. 1/3rd of the seeds land in water and die. 1/6 of the starting number are eaten by insects. Half the remainder sprout and are immediately eaten. How many dandelions survive long enough to flower?"""
    # Define the initial number of dandelion seeds
    initial_seeds = 300

    # Calculate the number of seeds that land in water and die
    dead_seeds = initial_seeds / 3

    # Calculate the number of seeds eaten by insects
    eaten_seeds = initial_seeds / 6

    # Calculate the number of sprouted seeds that are immediately eaten
    sprouted_seeds = (initial_seeds - dead_seeds - eaten_seeds) / 2

    # Calculate the number of surviving seeds that will eventually flower
    surviving_seeds = initial_seeds - dead_seeds - eaten_seeds - sprouted_seeds

    result = surviving_seeds
    return result

print(solution())