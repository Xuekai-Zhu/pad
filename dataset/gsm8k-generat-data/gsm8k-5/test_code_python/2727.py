def solution():
    total_seeds = 200  # Oshea has 200 basil seeds
    large_planter_capacity = 20  # The large planters can hold 20 seeds each
    small_planter_capacity = 4  # The small planters can hold 4 seeds each
    num_large_planters = 4  # Oshea has 4 large planters

    # Calculate the number of seeds that can be planted in the large planters
    large_planter_seeds = num_large_planters * large_planter_capacity

    # Calculate the remaining seeds that need to be planted in small planters
    remaining_seeds = total_seeds - large_planter_seeds

    # Calculate the number of small planters required
    num_small_planters = remaining_seeds / small_planter_capacity
    result = num_small_planters
    return result

print(solution())