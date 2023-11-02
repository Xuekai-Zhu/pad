def solution():
    # Calculate the total number of bread slices needed for 8 sandwiches
    total_slices = 8 * 2  # each sandwich uses two slices of bread

    # Calculate the number of bread packs needed
    packs_needed = (total_slices + 3) // 4  # round up to the nearest pack, each pack has 4 slices of bread

    result = packs_needed
    return result

print(solution())