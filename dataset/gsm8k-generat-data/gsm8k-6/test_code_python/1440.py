def solution():
    # Calculate the total number of points earned by Team Soccer Stars
    points_from_wins = 14 * 3  # 3 points for a win
    points_from_draws = (20 - 14 - 2) * 1  # 1 point for a draw
    total_points = points_from_wins + points_from_draws
    result = total_points
    return result

print(solution())