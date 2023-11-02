def solution():
    current_points_per_game = 26
    total_games = 20
    current_total_points = current_points_per_game * 15
    desired_total_points = 30 * 20
    remaining_points = desired_total_points - current_total_points
    remaining_games = total_games - 15
    points_per_game_needed = remaining_points / remaining_games
    result = points_per_game_needed
    return result

print(solution())