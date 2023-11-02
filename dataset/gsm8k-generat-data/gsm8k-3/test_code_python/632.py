def solution():
    """Yeon has three times as many watermelon seeds as Gwi. Gwi has 40 more watermelon seeds than Bom. If Bom has 300 watermelon seeds, how many seeds do they have together?"""
    # Find the number of seeds Gwi has
    gwi_seeds = 300 + 40

    # Find the number of seeds Yeon has
    yeon_seeds = 3 * gwi_seeds

    # Find the total number of seeds
    total_seeds = yeon_seeds + gwi_seeds + 300

    # Display the total number of seeds
    result = total_seeds
    return result

print(solution())