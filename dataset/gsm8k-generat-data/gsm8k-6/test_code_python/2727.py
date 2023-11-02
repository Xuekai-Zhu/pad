def solution():
    seeds = 200  # number of basil seeds
    large_planters = 4  # number of large planters
    small_planters_needed = (seeds - (large_planters * 20)) / 4  # calculate the number of small planters needed
    if small_planters_needed > int(small_planters_needed):  # round up if a fraction of a small planter is needed
        small_planters_needed = int(small_planters_needed) + 1 
    else:
        small_planters_needed = int(small_planters_needed)
    result = small_planters_needed
    return result

print(solution())