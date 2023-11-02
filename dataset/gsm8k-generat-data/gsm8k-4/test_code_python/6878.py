def solution():
    """Lolita has 54000 strawberry seeds. In each planting zone, 3123 seeds will be used. If she will accumulate 7 planting zones, how many strawberry seeds will remain?"""
    # Define the number of strawberry seeds and seeds used per planting zone
    total_seeds = 54000
    seeds_per_zone = 3123

    # Calculate the total number of seeds used in all planting zones
    total_seeds_used = seeds_per_zone * 7

    # Calculate the remaining number of seeds
    remaining_seeds = total_seeds - total_seeds_used

    # Return the result
    result = remaining_seeds
    return result

print(solution())