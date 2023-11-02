def solution():
    
    eggplant_seeds = 10
    pots = 4
    seeds_per_pot = 3
    seeds_planted = (pots - 1) * seeds_per_pot 
    seeds_left = eggplant_seeds - seeds_planted
    seeds_planted_in_fourth_pot = seeds_left % seeds_per_pot
    result = seeds_planted_in_fourth_pot
    return result

print(solution())