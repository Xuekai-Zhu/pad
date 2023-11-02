def solution():
    petals_per_daisy = 8  # Each daisy has 8 petals
    initial_daisies = 5  # Mabel starts with 5 daisies
    daisies_given_away = 2  # Mabel gives away 2 daisies

    # Calculate the total number of petals on the remaining daisies
    remaining_daisies = initial_daisies - daisies_given_away
    total_petals = remaining_daisies * petals_per_daisy
    result = total_petals
    return result

print(solution())