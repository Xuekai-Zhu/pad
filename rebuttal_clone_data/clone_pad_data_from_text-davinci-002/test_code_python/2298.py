def solution():
    seeds = 10
    pots = 4
    seeds_in_pot = 3
    seeds_in_fourth_pot = seeds - (seeds_in_pot * (pots - 1))
    result = seeds_in_fourth_pot
    return result

print(solution())