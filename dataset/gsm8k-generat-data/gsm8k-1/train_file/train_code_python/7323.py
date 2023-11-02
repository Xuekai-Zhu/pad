def solution():
    """This weekend's football game matched the Seattle Seahawks with the Denver Broncos. The final score was 37-23, with the Seattle Seahawks taking the win. If a touchdown is worth 7 points and a field goal is worth 3 points, how many touchdowns did the Seattle Seahawks score if they scored 3 field goals during the game?"""
    seahawks_score = 37
    field_goals = 3
    field_goal_points = 3
    touchdown_points = 7
    total_points_from_field_goals = field_goals * field_goal_points
    points_from_touchdowns = seahawks_score - total_points_from_field_goals
    touchdowns_scored = points_from_touchdowns // touchdown_points
    result = touchdowns_scored
    return result

print(solution())