def solution():
    total_seeds_collected = (4 * 6) + (3 * 2) + (9 * 3)  # total seeds from collected fruits
    target_num_seeds = 60
    remaining_num_seeds = target_num_seeds - total_seeds_collected
    result = remaining_num_seeds
    return result

print(solution())