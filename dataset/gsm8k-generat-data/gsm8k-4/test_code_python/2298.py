def solution():
    """Eunice has 10 eggplant seeds and 4 pots. How many seeds will be planted in the fourth pot if 3 seeds can be planted in 1 pot?"""
    # Define the number of seeds and pots
    eggplant_seeds = 10
    pots = 4

    # Calculate the total number of seeds that can be planted
    total_seeds = pots * 3

    # Calculate the number of seeds that will be planted in the fourth pot
    seeds_in_fourth_pot = eggplant_seeds - total_seeds

    # return the result
    result = seeds_in_fourth_pot
    return result

print(solution())