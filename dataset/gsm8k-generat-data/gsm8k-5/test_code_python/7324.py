def solution():
    score_seahawks = 37  # The Seattle Seahawks scored 37 points
    score_broncos = 23  # The Denver Broncos scored 23 points
    field_goals = 3  # The Seattle Seahawks scored 3 field goals

    # Calculate the total points scored by touchdowns
    touchdown_points = score_seahawks - (field_goals * 3)

    # Calculate the number of touchdowns scored
    touchdowns = touchdown_points // 7
    result = touchdowns
    return result

print(solution())