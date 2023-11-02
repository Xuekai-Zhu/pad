def solution():
    """Connor scored 2 in a game while Amy scored 4 more than Connor. Jason scored twice the score of Amy. If Connor, Amy, and Jason belong to the same team, how many points did their team have?"""
    # Calculate Amy's score
    amy_score = 2 + 4

    # Calculate Jason's score
    jason_score = amy_score * 2

    # Calculate the total team score
    team_score = 2 + amy_score + jason_score

    result = team_score
    return result

print(solution())