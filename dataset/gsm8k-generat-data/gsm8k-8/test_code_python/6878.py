def solution():
    # Define the total number of strawberry seeds and number of seeds used in each planting zone
    total_seeds = 54000
    seeds_per_zone = 3123

    # Calculate the total number of seeds used in all planting zones
    total_seeds_used = seeds_per_zone * 7

    # Calculate the number of seeds remaining
    seeds_remaining = total_seeds - total_seeds_used
    result = seeds_remaining
    return result

print(solution())