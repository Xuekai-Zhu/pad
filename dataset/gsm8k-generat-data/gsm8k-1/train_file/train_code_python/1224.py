def solution():
    """Donovan Mitchell is currently averaging 26 points per game. His team has played 15 games this season. He has a goal of averaging 30 points per game for the entire 20 game season. How many points does he need to average per game to reach his goal?"""
    current_points = 26 * 15
    total_points_needed = 30 * 20
    points_needed_per_game = (total_points_needed - current_points) / (20 - 15)
    result = points_needed_per_game
    return result

print(solution())