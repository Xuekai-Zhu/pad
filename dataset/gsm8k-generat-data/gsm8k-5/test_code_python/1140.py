def solution():
    total_games = 50  # 40 games played + 10 games to play
    win_percent = 0.7  # The team won 70% of their games
    win_games = total_games * win_percent  # Total number of games won
    remaining_win_games = 0.6 * total_games  # Number of games the team needs to win to have a 60% overall win rate
    remaining_games = total_games - win_games  # Number of games the team has left to play

    # Calculate the number of games the team can lose and still reach their goal
    lose_games = remaining_games - (remaining_win_games - win_games)
    result = lose_games
    return result

print(solution())