def solution():
    """In a basketball game, Tobee scored 4 points. Jay scored 6 more than Tobee and Sean scored 2 less than the points of Tobee and Jay together.
    If Tobee, Jay, and Sean are on the same team, how many points did they score for their team?"""
    tobee_points = 4
    jay_points = tobee_points + 6
    sean_points = (tobee_points + jay_points) - 2
    total_points = tobee_points + jay_points + sean_points
    result = total_points
    return result

print(solution())