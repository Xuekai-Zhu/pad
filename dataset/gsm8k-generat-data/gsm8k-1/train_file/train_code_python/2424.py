def solution():
    """Mabel has 5 daisies in her garden, and each daisy has 8 petals. If she gives 2 daisies to her teacher, how many petals does she have on the remaining daisies in her garden?"""
    daisies_in_garden = 5
    petals_per_daisy = 8
    daisies_given = 2
    remaining_daisies = daisies_in_garden - daisies_given
    remaining_petals = remaining_daisies * petals_per_daisy
    result = remaining_petals
    return result

print(solution())