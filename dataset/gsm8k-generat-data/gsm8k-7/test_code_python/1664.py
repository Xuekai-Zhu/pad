def solution():
    num_matches_first_round = 6
    num_matches_second_round = 6
    num_matches_last_round = 4

    # Calculate the total number of matches won in the first two rounds
    num_wins_first_two_rounds = num_matches_first_round * 2

    # Calculate the total number of wins in the last round
    num_wins_last_round = num_matches_last_round / 2

    # Calculate the total number of wins in the entire competition
    total_wins = num_wins_first_two_rounds + num_wins_last_round

    result = total_wins
    return result

print(solution())