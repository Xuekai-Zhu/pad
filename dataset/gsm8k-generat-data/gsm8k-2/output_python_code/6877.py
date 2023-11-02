def solution():
    """Lolita has 54000 strawberry seeds. In each planting zone, 3123 seeds will be used. If she will accumulate 7 planting zones, how many strawberry seeds will remain?"""
    total_seeds = 54000
    seeds_per_zone = 3123
    zones = 7
    seeds_used = seeds_per_zone * zones
    seeds_remaining = total_seeds - seeds_used
    result = seeds_remaining
    return result

print(solution())