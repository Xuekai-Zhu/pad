def solution():
    """Mabel has 5 daisies in her garden, and each daisy has 8 petals. If she gives 2 daisies to her teacher, how many petals does she have on the remaining daisies in her garden?"""
    total_daisies = 5
    petals_per_daisy = 8
    daisies_given = 2
    remaining_daisies = total_daisies - daisies_given
    remaining_petals = remaining_daisies * petals_per_daisy
    result = remaining_petals
    return result

print(solution())