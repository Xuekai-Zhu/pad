def solution():
    total_games = 75  # 50 games played + 25 games left
    current_wins = 35  # The team has already won 35 games
    current_win_percentage = (current_wins / 50) * 100  # Calculate the current win percentage
    remaining_games = 25  # The team still has 25 games left to play
    desired_win_percentage = 64  # The desired win percentage for the entire season

    # Solve for the number of remaining games the team needs to win to achieve the desired win percentage for the entire season
    required_wins = round((total_games * (desired_win_percentage / 100)) - current_wins)
    remaining_wins_needed = required_wins - current_wins
    remaining_games_left = remaining_games - required_wins

    # Check if it's possible to win the remaining games to achieve the desired win percentage
    if remaining_games_left < 0 or remaining_wins_needed < 0:
        result = "It is not possible to achieve a 64% win percentage for the entire season."
    else:
        result = remaining_wins_needed
    return result

print(solution())