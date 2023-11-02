def solution():
    alyssa_cans = 30
    abigail_cans = 43
    total_cans_needed = 100

    # Calculate the total number of cans they need to collect.
    total_cans_collected = alyssa_cans + abigail_cans

    # Calculate how many more cans they need to collect.
    cans_left = total_cans_needed - total_cans_collected
    result = cans_left
    return result

print(solution())