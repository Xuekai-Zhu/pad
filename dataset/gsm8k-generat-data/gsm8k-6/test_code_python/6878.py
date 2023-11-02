def solution():
    # Calculate the total number of seeds used in all 7 planting zones
    total_seeds_used = 3123 * 7

    # Calculate the number of seeds that will remain
    seeds_remaining = 54000 - total_seeds_used
    result = seeds_remaining
    return result

print(solution())