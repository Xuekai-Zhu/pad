def solution():
    
    apple_seeds = 6
    pear_seeds = 2
    grape_seeds = 3
    collected_apple_seeds = 4 * apple_seeds
    collected_pear_seeds = 3 * pear_seeds
    collected_grape_seeds = 9 * grape_seeds
    total_seeds_collected = collected_apple_seeds + collected_pear_seeds + collected_grape_seeds
    seeds_left = 60 - total_seeds_collected
    result = seeds_left
    return result

print(solution())