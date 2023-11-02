def solution():
    total_seeds = 54000  # Lolita has 54000 strawberry seeds
    seeds_per_zone = 3123  # Each planting zone requires 3123 seeds
    num_zones = 7  # Lolita will use 7 planting zones

    # Calculate the total number of seeds used
    total_seeds_used = seeds_per_zone * num_zones

    # Calculate the number of seeds remaining
    seeds_remaining = total_seeds - total_seeds_used
    result = seeds_remaining
    return result

print(solution())