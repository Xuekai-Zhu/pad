def solution():
    # Calculate the number of matches won in the first 100 matches
    matches_won_first_100 = 0.5 * 100

    # Calculate the number of matches won in the next 100 matches
    matches_won_next_100 = 0.6 * 100

    # Calculate the total number of matches that Sam won
    total_matches_won = matches_won_first_100 + matches_won_next_100
    result = total_matches_won
    return result

print(solution())