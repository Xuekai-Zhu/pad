def solution():
    max_points = 5
    dulce_points = 3
    val_points = 2 * (max_points + dulce_points)
    total_points = max_points + dulce_points + val_points
    opponents_total_points = 40
    points_behind = opponents_total_points - total_points
    result = points_behind
    return result

print(solution())