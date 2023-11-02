def solution():
    # Calculate the total number of points scored by the Seattle Seahawks
    total_points = 37  
    field_goals_scored = 3  
    field_goal_points = 3  
    total_points_from_field_goals = field_goals_scored * field_goal_points  
    points_from_touchdowns = total_points - total_points_from_field_goals  
    touchdowns_scored = points_from_touchdowns // 7  
    result = touchdowns_scored
    return result

print(solution())