def solution():
    tall_hills = 2
    small_hills = 3
    tall_sleds = 4
    small_sleds = tall_sleds / 2

    # Calculate the total number of sleds on the tall hills
    total_tall_sleds = tall_hills * tall_sleds

    # Calculate the total number of sleds on the small hills
    total_small_sleds = small_hills * small_sleds

    # Calculate the total number of sleds
    total_sleds = total_tall_sleds + total_small_sleds
    result = total_sleds
    return result

print(solution())