def solution():
    """Darius, Matt, and Marius are friends, who played table football. During all the games they played, Marius scored 3 points more than Darius, and Darius scored 5 points less than Matt. How many points did all three friends score together, if Darius scored 10 points?"""
    darius_score = 10
    matt_score = darius_score + 5
    marius_score = darius_score + 3
    total_score = darius_score + matt_score + marius_score
    result = total_score
    return result

print(solution())