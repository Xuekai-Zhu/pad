def solution():
    """Zara bought 24 cows, 7 sheep, and some goats. Next week, she will transport all of them to a new farm in 3 equally-sized groups of 48 animals per group. How many goats does she own?"""
    total_animals = 24 + 7 + x
    total_groups = 3
    group_size = 48
    goats = (total_animals - (total_groups * group_size)) / total_groups
    result = goats
    return result

print(solution())