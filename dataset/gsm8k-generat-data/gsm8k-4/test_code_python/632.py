def solution():
    """Yeon has three times as many watermelon seeds as Gwi. Gwi has 40 more watermelon seeds than Bom. If Bom has 300 watermelon seeds, how many seeds do they have together?"""
    # Define the number of watermelon seeds Bom has
    bom_seeds = 300

    # Calculate the number of watermelon seeds Gwi has
    gwi_seeds = bom_seeds + 40

    # Calculate the number of watermelon seeds Yeon has
    yeon_seeds = 3 * gwi_seeds

    # Calculate the total number of watermelon seeds
    total_seeds = bom_seeds + gwi_seeds + yeon_seeds

    # return the result
    result = total_seeds
    return result

print(solution())