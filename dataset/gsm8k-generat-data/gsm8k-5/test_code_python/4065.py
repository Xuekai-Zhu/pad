def solution():
    max_points = 5
    dulce_points = 3
    val_points = 2 * (max_points + dulce_points)  # Val has twice the combined points of Max and Dulce
    total_team_points = max_points + dulce_points + val_points
    opponents_points = 40
    points_behind = opponents_points - total_team_points
    result = points_behind
    return result

print(solution())