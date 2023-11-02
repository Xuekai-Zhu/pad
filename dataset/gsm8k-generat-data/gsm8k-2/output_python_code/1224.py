def solution():
    """Donovan Mitchell is currently averaging 26 points per game. His team has played 15 games this season. He has a goal of averaging 30 points per game for the entire 20 game season. How many points does he need to average per game to reach his goal?"""
    current_average = 26
    remaining_games = 20 - 15
    total_points_needed = 30 * 20
    points_already_scored = current_average * 15
    points_needed = total_points_needed - points_already_scored
    average_needed = points_needed / remaining_games
    result = average_needed
    return result

print(solution())