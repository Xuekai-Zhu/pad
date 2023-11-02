def solution():
    """This weekend's football game matched the Seattle Seahawks with the Denver Broncos. The final score was 37-23, with the Seattle Seahawks taking the win. If a touchdown is worth 7 points and a field goal is worth 3 points, how many touchdowns did the Seattle Seahawks score if they scored 3 field goals during the game?"""
    seattle_score = 37
    denver_score = 23
    field_goals = 3
    touchdown_points = 7
    field_goal_points = 3
    seattle_touchdowns = (seattle_score - (field_goals * field_goal_points)) / touchdown_points
    result = seattle_touchdowns
    return result

print(solution())