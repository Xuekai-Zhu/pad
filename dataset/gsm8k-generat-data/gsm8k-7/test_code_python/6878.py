def solution():
    total_seeds = 54000
    seeds_per_zone = 3123
    num_zones = 7

    # Calculate the total number of seeds used in all planting zones
    total_seeds_used = seeds_per_zone * num_zones

    # Calculate the number of seeds that will remain
    num_seeds_remaining = total_seeds - total_seeds_used
    result = num_seeds_remaining
    return result

print(solution())