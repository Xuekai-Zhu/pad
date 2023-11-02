def solution():
    """Zara bought 24 cows, 7 sheep, and some goats. Next week, she will transport all of them to a new farm in 3 equally-sized groups of 48 animals per group. How many goats does she own?"""
    cows = 24
    sheep = 7
    total_animals = cows + sheep + x
    groups = 3
    animals_per_group = 48
    goats = (groups * animals_per_group) - cows - sheep
    result = goats
    return result

print(solution())