def solution():
    tall_hills = 2  # Wilson sleds down 2 tall hills
    small_hills = 3  # Wilson sleds down 3 small hills
    sleds_per_tall_hill = 4  # Wilson sleds down each tall hill 4 times
    sleds_per_small_hill = sleds_per_tall_hill / 2  # Wilson sleds down each small hill half as often as the tall hills

    # Calculate the total number of times Wilson sleds down the tall hills
    total_sleds_tall_hills = tall_hills * sleds_per_tall_hill

    # Calculate the total number of times Wilson sleds down the small hills
    total_sleds_small_hills = small_hills * sleds_per_small_hill

    # Calculate the total number of times Wilson sleds down all the hills
    total_sleds = total_sleds_tall_hills + total_sleds_small_hills
    result = total_sleds
    return result

print(solution())