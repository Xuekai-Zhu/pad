def solution():
    """Eunice has 10 eggplant seeds and 4 pots. How many seeds will be planted in the fourth pot if 3 seeds can be planted in 1 pot?"""
    # Define the number of eggplant seeds and pots
    NUM_SEEDS = 10
    NUM_POTS = 4
    SEEDS_PER_POT = 3

    # Calculate the total number of seeds that can be planted
    total_seeds = NUM_POTS * SEEDS_PER_POT

    # Calculate the number of seeds that will be planted in the fourth pot
    seeds_in_fourth_pot = NUM_SEEDS - total_seeds

    # Display the number of seeds in the fourth pot
    result = seeds_in_fourth_pot
    return result

print(solution())