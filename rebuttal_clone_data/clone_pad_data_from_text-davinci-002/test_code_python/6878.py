def solution():
    total_seeds = 54000
    seeds_used = 3123
    total_zones = 7
    seeds_remaining = total_seeds - (seeds_used * total_zones)
    result = seeds_remaining
    return result

print(solution())