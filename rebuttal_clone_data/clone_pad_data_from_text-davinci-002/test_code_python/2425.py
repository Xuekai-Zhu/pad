def solution():
    daisies_in_garden = 5
    petals_on_daisy = 8
    daisies_given_away = 2
    remaining_daisies = daisies_in_garden - daisies_given_away
    remaining_petals = remaining_daisies * petals_on_daisy
    result = remaining_petals
    return result

print(solution())