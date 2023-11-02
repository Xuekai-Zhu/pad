def solution():
    # Calculate the total number of times Wilson sleds down the hills
    tall_hills = 2  # number of tall hills
    small_hills = 3  # number of small hills
    sleds_tall_hills = 4 * tall_hills  # Wilson sleds down tall hills 4 times each
    sleds_small_hills = 0.5 * sleds_tall_hills * small_hills  # Wilson sleds down small hills half as often as tall hills
    total_sleds = sleds_tall_hills + sleds_small_hills  # total number of sleds
    result = total_sleds
    return result

print(solution())