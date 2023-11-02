def solution():
    """Yeon has three times as many watermelon seeds as Gwi. Gwi has 40 more watermelon seeds than Bom. If Bom has 300 watermelon seeds, how many seeds do they have together?"""
    bom_seeds = 300
    gwi_seeds = bom_seeds + 40
    yeon_seeds = 3 * gwi_seeds
    total_seeds = bom_seeds + gwi_seeds + yeon_seeds
    result = total_seeds
    return result

print(solution())