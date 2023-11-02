def solution():
    seeds_left = 30
    seeds_to_left_birds = 20
    seeds_to_right_birds = seeds_to_left_birds * 2
    additional_seeds = 30
    total_seeds = seeds_left + seeds_to_left_birds + seeds_to_right_birds + additional_seeds
    result = total_seeds
    return result

print(solution())