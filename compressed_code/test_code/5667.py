def solution():
    
    seattle_score = 37
    denver_score = 23
    field_goals = 3
    touchdown_points = 7
    field_goal_points = 3
    seattle_touchdowns = (seattle_score - (field_goals * field_goal_points)) / touchdown_points
    result = seattle_touchdowns
    return result

print(solution())