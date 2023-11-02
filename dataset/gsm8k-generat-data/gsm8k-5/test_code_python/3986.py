def solution():
    sweets_per_child = 4  # Each child takes 4 sweets
    remaining_fraction = 1/3  # After taking 4 sweets each, there is still 1/3 of the original amount left

    # Calculate the total number of sweets left after the children each took 4 sweets
    total_sweets_left = 48 * sweets_per_child + 48 * sweets_per_child * remaining_fraction

    # Calculate the original number of sweets in the pack
    original_sweets = total_sweets_left / (1 - remaining_fraction)
    result = original_sweets
    return result

print(solution())