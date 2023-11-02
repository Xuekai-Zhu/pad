def solution():
    # Define number of sets used per show and sets given away per show
    sets_per_show = 5
    sets_given_away = 6

    # Calculate total sets used and given away for 30 nights
    total_sets_used = 30 * sets_per_show
    total_sets_given_away = 30 * sets_given_away

    # Calculate the final result
    result = total_sets_used + total_sets_given_away
    return result

print(solution())