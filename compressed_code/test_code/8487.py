def solution():
    
    seeds_left = 30
    left_birds_seeds = 20
    right_birds_seeds = 2 * left_birds_seeds
    total_seeds = seeds_left + left_birds_seeds + right_birds_seeds + 30
    result = total_seeds
    return result

print(solution())