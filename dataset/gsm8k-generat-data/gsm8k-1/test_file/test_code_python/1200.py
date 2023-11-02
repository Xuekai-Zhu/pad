def solution():
    """Twenty tourists discovered 700 shells in a strip mall parking lot. They had divided into three groups, Alphas, The finders, and Gogetters to find as many shells as possible. If team Alphas found 40% of the shells, and team The finders found 60% of the remaining shells, how many shells did team Gogetters find?"""
    total_shells = 700
    alpha_percent = 0.4
    alpha_shells = total_shells * alpha_percent
    remaining_shells = total_shells - alpha_shells
    finder_percent = 0.6
    finder_shells = remaining_shells * finder_percent
    gogetter_shells = total_shells - alpha_shells - finder_shells
    result = gogetter_shells
    return result

print(solution())