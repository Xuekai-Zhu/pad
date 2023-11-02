def solution():
    """In a basketball game, Jon scored 3 points. Jack scored 5 points more than Jon, and Tom scored 4 less than the points of Jon and Jack together. How many points did they score altogether?"""
    jon_points = 3
    jack_points = jon_points + 5
    jon_and_jack_points = jon_points + jack_points
    tom_points = jon_and_jack_points - 4
    total_points = jon_points + jack_points + tom_points
    result = total_points
    return result

print(solution())