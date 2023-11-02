def solution():
    
    total_seeds = 10
    total_pots = 4
    seeds_per_pot = 3
    seeds_planted = (total_pots - 1) * seeds_per_pot
    seeds_leftover = total_seeds - seeds_planted
    seeds_in_fourth_pot = seeds_leftover % seeds_per_pot
    result = seeds_in_fourth_pot
    return result

print(solution())