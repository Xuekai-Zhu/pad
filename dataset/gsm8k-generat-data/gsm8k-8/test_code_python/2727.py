def solution():
    # Calculate the total number of seeds that can be planted in large planters
    large_planter_seeds = 4 * 20

    # Calculate the number of seeds remaining after filling the large planters
    remaining_seeds = 200 - large_planter_seeds

    # Calculate the number of small planters needed for the remaining seeds
    small_planter_count = remaining_seeds / 4
    small_planter_count = math.ceil(small_planter_count)

    result = small_planter_count
    return result

print(solution())