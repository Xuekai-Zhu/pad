def solution():
    slices_per_watermelon = 40
    seeds_per_slice = 20 + 20  # 20 black seeds + 20 white seeds

    # Calculate the total number of seeds in a watermelon
    total_seeds = slices_per_watermelon * seeds_per_slice
    result = total_seeds
    return result

print(solution())