def solution():
    seeds_per_pot = 3  # 3 seeds can be planted in 1 pot
    pots = 4  # Eunice has 4 pots
    total_seeds = 10  # Eunice has 10 eggplant seeds

    # Calculate the number of seeds that can be planted in each pot
    seeds_per_pot = total_seeds // pots

    # Calculate how many seeds will be planted in the fourth pot
    seeds_in_fourth_pot = total_seeds - seeds_per_pot * (pots - 1)
    result = seeds_in_fourth_pot
    return result

print(solution())