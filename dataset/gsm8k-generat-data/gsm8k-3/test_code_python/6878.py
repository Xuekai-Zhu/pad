def solution():
    """Lolita has 54000 strawberry seeds. In each planting zone, 3123 seeds will be used. If she will accumulate 7 planting zones, how many strawberry seeds will remain?"""
    # Define the total number of strawberry seeds
    total_seeds = 54000

    # Define the number of seeds used per planting zone
    seeds_per_zone = 3123

    # Calculate the total number of seeds used in all planting zones
    total_seeds_used = seeds_per_zone * 7

    # Calculate the number of seeds remaining
    seeds_remaining = total_seeds - total_seeds_used

    # Display the number of seeds remaining
    result = seeds_remaining
    return result

print(solution())