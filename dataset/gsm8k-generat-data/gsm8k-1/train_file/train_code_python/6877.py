def solution():
    """Lolita has 54000 strawberry seeds. In each planting zone, 3123 seeds will be used. If she will accumulate 7 planting zones, how many strawberry seeds will remain?"""
    total_seeds = 54000
    seeds_per_zone = 3123
    zones = 7
    used_seeds = seeds_per_zone * zones
    remaining_seeds = total_seeds - used_seeds
    result = remaining_seeds
    return result

print(solution())