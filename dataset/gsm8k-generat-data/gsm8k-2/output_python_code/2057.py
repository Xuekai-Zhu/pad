def solution():
    """In a basketball game, Tobee scored 4 points. Jay scored 6 more than Tobee and Sean scored 2 less than the points of Tobee and Jay together. If Tobee, Jay, and Sean are on the same team, how many points did they score for their team?"""
    tobee_score = 4
    jay_score = tobee_score + 6
    sean_score = (tobee_score + jay_score) - 2
    total_score = tobee_score + jay_score + sean_score
    result = total_score
    return result

print(solution())