def solution():
    
    slices = 40
    black_seeds_per_slice = 20
    white_seeds_per_slice = 20
    total_seeds_per_slice = black_seeds_per_slice + white_seeds_per_slice
    total_seeds = slices * total_seeds_per_slice
    result = total_seeds
    return result

print(solution())