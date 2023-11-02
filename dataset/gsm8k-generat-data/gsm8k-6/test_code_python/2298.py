def solution():
    # Calculate the number of seeds that can be planted in the 4 pots
    seeds_per_pot = 3
    seeds_planted = (4-1) * seeds_per_pot # we subtract 1 since 3 seeds have already been planted in the first three pots
    seeds_remaining = 10 - seeds_planted
    seeds_in_fourth_pot = min(seeds_remaining, seeds_per_pot)

    result = seeds_in_fourth_pot
    return result

print(solution())