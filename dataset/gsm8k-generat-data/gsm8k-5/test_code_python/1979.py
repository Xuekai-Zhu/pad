def solution():
    slices_per_watermelon = 40  # Val cuts a single watermelon into 40 slices
    seeds_per_slice = 20 + 20  # Each slice has 20 black seeds and 20 white seeds

    # Calculate the total number of seeds in a watermelon
    total_seeds = slices_per_watermelon * seeds_per_slice
    result = total_seeds
    return result

print(solution())