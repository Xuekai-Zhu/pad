def solution():
    num_daisies = 5
    petals_per_daisy = 8
    num_given_away = 2

    # Calculate the total number of petals on all daisies
    total_petals = num_daisies * petals_per_daisy

    # Calculate the number of petals on the daisies that Mabel kept
    remaining_daisies = num_daisies - num_given_away
    remaining_petals = remaining_daisies * petals_per_daisy

    result = remaining_petals
    return result

print(solution())