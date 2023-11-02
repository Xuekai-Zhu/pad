def solution():
    """A farmer has twice as many pigs as cows, and 4 more cows than goats. If the farmer has 56 animals total, how many goats does he have?"""
    total_animals = 56
    # Let's use g for goats, c for cows, and p for pigs
    c = g + 4
    p = 2*c
    g + c + p = total_animals
    g + (g+4) + 2*(g+4) = total_animals
    g = (total_animals - 12) / 5
    result = g
    return result

print(solution())