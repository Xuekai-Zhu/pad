def solution():
    
    total_daisies = 5
    petals_per_daisy = 8
    daisies_given = 2
    remaining_daisies = total_daisies - daisies_given
    remaining_petals = remaining_daisies * petals_per_daisy
    result = remaining_petals
    return result

print(solution())