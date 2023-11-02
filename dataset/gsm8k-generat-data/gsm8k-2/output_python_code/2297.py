def solution():
    """Eunice has 10 eggplant seeds and 4 pots. How many seeds will be planted in the fourth pot if 3 seeds can be planted in 1 pot?"""
    total_seeds = 10
    total_pots = 4
    seeds_per_pot = 3
    seeds_planted = (total_pots - 1) * seeds_per_pot
    seeds_leftover = total_seeds - seeds_planted
    seeds_in_fourth_pot = seeds_leftover % seeds_per_pot
    result = seeds_in_fourth_pot
    return result

print(solution())