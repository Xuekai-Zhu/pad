def solution():
    """A farmer has twice as many pigs as cows, and 4 more cows than goats. If the farmer has 56 animals total, how many goats does he have?"""
    total_animals = 56
    pigs_cows_ratio = 2
    cows_goats_diff = 4

    # Let's solve for goats using the equations: 
    # pigs = 2 * cows
    # cows = goats + cows_goats_diff
    # pigs + cows + goats = total_animals

    cows = (total_animals / (pigs_cows_ratio + 1 + 1 + cows_goats_diff)) * (1 + cows_goats_diff)
    goats = cows - cows_goats_diff
    pigs = 2 * cows

    result = goats
    return result

print(solution())