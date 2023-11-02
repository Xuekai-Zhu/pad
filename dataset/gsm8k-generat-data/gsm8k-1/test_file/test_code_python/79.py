def solution():
    """Dan plants 3 rose bushes. Each rose bush has 25 roses. Each rose has 8 thorns. How many thorns are there total?"""
    rose_bushes = 3
    roses_per_bush = 25
    thorns_per_rose = 8
    total_thorns = rose_bushes * roses_per_bush * thorns_per_rose
    result = total_thorns
    return result

print(solution())