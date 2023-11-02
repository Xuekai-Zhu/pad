def solution():
    total_points = 37
    points_from_field_goals = 3 * 3
    points_from_touchdowns = total_points - points_from_field_goals
    result = points_from_touchdowns / 7
    
    return result

print(solution())