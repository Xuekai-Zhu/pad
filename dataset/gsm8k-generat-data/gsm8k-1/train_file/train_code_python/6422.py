def solution():
    """A basketball team won 35 out of the 50 games that they have played. They still have 25 games left to play for the season. How many of the remaining games must they win so that their percentage of wins in the entire season is 64%?"""
    total_games = 75
    current_wins = 35
    remaining_games = 25
    target_percentage = 64
    target_wins = total_games * (target_percentage / 100)
    remaining_wins = target_wins - current_wins
    needed_win_percentage = remaining_wins / remaining_games
    result = needed_win_percentage * 100
    return result

print(solution())