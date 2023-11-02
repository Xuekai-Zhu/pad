def solution():
    """Eunice has 10 eggplant seeds and 4 pots. How many seeds will be planted in the fourth pot if 3 seeds can be planted in 1 pot?"""
    eggplant_seeds = 10
    pots = 4
    seeds_per_pot = 3
    seeds_planted = (pots - 1) * seeds_per_pot # only counting the first three pots
    seeds_left = eggplant_seeds - seeds_planted
    seeds_planted_in_fourth_pot = seeds_left % seeds_per_pot
    result = seeds_planted_in_fourth_pot
    return result

print(solution())