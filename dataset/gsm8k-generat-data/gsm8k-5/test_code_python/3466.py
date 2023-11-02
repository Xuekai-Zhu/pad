def solution():
    total_points = 720  # UF scored a total of 720 points in 24 games
    average_points_per_game = total_points / 24  # UF's average points per game

    # Calculate the number of points the opponent scored
    opponent_points = (average_points_per_game / 2) - 2
    result = opponent_points
    return result

print(solution())