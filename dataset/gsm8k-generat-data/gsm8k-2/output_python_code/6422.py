def solution():
    """A basketball team won 35 out of the 50 games that they have played. They still have 25 games left to play for the season. How many of the remaining games must they win so that their percentage of wins in the entire season is 64%?"""
    total_games = 50 + 25
    desired_percentage = 0.64
    # solve for total wins needed to get the desired percentage
    total_wins_needed = total_games * desired_percentage
    # solve for wins needed in remaining games
    remaining_wins_needed = total_wins_needed - 35
    # solve for remaining games
    remaining_games = 25
    # solve for wins per remaining game needed to meet desired percentage
    wins_per_game_needed = remaining_wins_needed / remaining_games
    result = int(wins_per_game_needed)
    return result

print(solution())