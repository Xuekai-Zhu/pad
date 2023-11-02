def solution():
    seahawks_score = 37
    broncos_score = 23
    touchdown_points = 7
    field_goal_points = 3

    # Calculate the total number of points the Seattle Seahawks scored
    seahawks_total_points = seahawks_score - (3 * field_goal_points)

    # Calculate the number of touchdowns the Seattle Seahawks scored
    seahawks_touchdowns = seahawks_total_points // touchdown_points

    result = seahawks_touchdowns
    return result

print(solution())