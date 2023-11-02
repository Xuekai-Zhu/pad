def solution():
    first_100_match_win_rate = 0.5
    second_100_match_win_rate = 0.6

    # Calculate the total number of matches won in the first 100 games
    num_matches_won_first_100 = first_100_match_win_rate * 100

    # Calculate the total number of matches won in the next 100 games
    num_matches_won_next_100 = second_100_match_win_rate * 100

    # Calculate the total number of matches won in all 200 games
    total_matches_won = num_matches_won_first_100 + num_matches_won_next_100
    result = total_matches_won
    return result

print(solution())