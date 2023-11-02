def solution():
    num_basil_seeds = 200
    large_planter_capacity = 20
    small_planter_capacity = 4

    # Calculate the number of large planters needed
    num_large_planters_needed = num_basil_seeds // large_planter_capacity

    # Calculate the remaining number of basil seeds
    remaining_basil_seeds = num_basil_seeds % large_planter_capacity

    # Calculate the number of small planters needed for the remaining basil seeds
    num_small_planters_needed = remaining_basil_seeds // small_planter_capacity

    # If there are any remaining basil seeds, one more small planter is needed
    if remaining_basil_seeds % small_planter_capacity != 0:
        num_small_planters_needed += 1

    # Calculate the total number of planters needed
    total_planters_needed = num_large_planters_needed + num_small_planters_needed
    result = total_planters_needed
    return result

print(solution())