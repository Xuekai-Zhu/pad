def solution():
    """Brendan has entered a kickboxing competition and wins matches against multiple contestants. He wins all of the matches in the first 2 rounds, each of which had 6 matches, then wins half of the 4 matches in the last round. How many matches did Brendan win throughout the competition?"""
    # Define the number of matches in each round
    round1_matches = 6
    round2_matches = 6
    round3_matches = 4

    # Calculate the number of matches won in the first 2 rounds
    matches_won_round1 = round1_matches
    matches_won_round2 = round2_matches
    total_matches_won_first_2_rounds = matches_won_round1 + matches_won_round2

    # Calculate the number of matches won in the last round
    matches_won_round3 = round3_matches / 2
    total_matches_won = total_matches_won_first_2_rounds + matches_won_round3

    # Return the total number of matches won
    result = total_matches_won
    return result

print(solution())