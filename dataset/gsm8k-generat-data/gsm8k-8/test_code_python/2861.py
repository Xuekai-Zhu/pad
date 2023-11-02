def solution():
    # Calculate how many games they need to win overall
    total_games = 20 + 10
    games_needed = 2/3 * total_games

    # Calculate how many games they need to win in the remaining 10 games
    remaining_games = 10
    games_already_won = 12
    games_left_to_win = games_needed - games_already_won

    result = games_left_to_win
    return result

print(solution())