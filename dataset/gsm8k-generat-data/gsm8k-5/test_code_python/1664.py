def solution():
    matches_per_round = 6  # The first 2 rounds each have 6 matches
    total_matches_first_two_rounds = 2 * matches_per_round  # Calculate the total matches in the first 2 rounds
    matches_last_round = 4  # The last round has 4 matches
    matches_won_last_round = matches_last_round / 2  # Brendan wins half of the matches in the last round

    # Calculate the total number of matches Brendan won
    total_matches_won = total_matches_first_two_rounds + matches_won_last_round
    result = total_matches_won
    return result

print(solution())