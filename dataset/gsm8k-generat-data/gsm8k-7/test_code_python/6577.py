def solution():
    passing_score = 50
    earned_points = 3 * 20
    lost_points = 5
    total_points = earned_points - lost_points

    # Calculate the minimum number of points Jimmy needs to pass
    min_passing_points = passing_score - total_points

    result = min_passing_points
    return result

print(solution())