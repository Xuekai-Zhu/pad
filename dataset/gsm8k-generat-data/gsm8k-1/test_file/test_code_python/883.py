def solution():
    """Jerry counts six birds nesting in the bushes, 2/3rd of that number of birds flying overhead, and 3 groups of eight birds each feeding. How many birds does he count in total?"""
    birds_nesting = 6
    birds_flying = birds_nesting * (2/3)
    birds_feeding = 3 * 8
    total_birds = birds_nesting + birds_flying + birds_feeding
    result = total_birds
    return result

print(solution())