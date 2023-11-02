def solution():
    # Calculate the number of total games in the season
    total_games = 50 + 25

    # Calculate the number of games they need to win for a 64% win rate
    win_rate = 0.64
    win_target = win_rate * total_games
    win_needed = win_target - 35

    # Calculate the number of remaining games they need to win
    games_left = 25
    games_needed_to_win = round(win_needed / games_left)

    result = games_needed_to_win
    return result

print(solution())