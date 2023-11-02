def solution():
    """Connor scored 2 in a game while Amy scored 4 more than Connor. Jason scored twice the score of Amy. If Connor, Amy, and Jason belong to the same team, how many points did their team have?"""
    connor_score = 2
    amy_score = connor_score + 4
    jason_score = amy_score * 2
    total_score = connor_score + amy_score + jason_score
    result = total_score
    return result

print(solution())