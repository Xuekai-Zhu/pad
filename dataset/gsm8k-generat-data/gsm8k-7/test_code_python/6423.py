def solution():
    num_wins = 35
    num_games_played = 50
    num_games_remaining = 25
    target_percentage = 0.64

    # Calculate the total number of games in the entire season
    total_num_games = num_games_played + num_games_remaining

    # Calculate the minimum number of wins needed to achieve the target percentage
    target_num_wins = total_num_games * target_percentage - num_wins

    # Calculate the number of wins needed in the remaining games
    num_remaining_wins_needed = target_num_wins - num_games_remaining * 0.5

    result = num_remaining_wins_needed
    return result

print(solution())