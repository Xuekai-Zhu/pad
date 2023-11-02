def solution():
    """Miggy's mom brought home 3 bags of birthday hats. Each bag has 15 hats. Miggy accidentally tore off 5 hats. During the party, only 25 hats were used. How many hats were unused?"""
    hats_per_bag = 15
    total_hats = hats_per_bag * 3
    torn_hats = 5
    used_hats = 25
    unused_hats = total_hats - torn_hats - used_hats
    result = unused_hats
    return result

print(solution())