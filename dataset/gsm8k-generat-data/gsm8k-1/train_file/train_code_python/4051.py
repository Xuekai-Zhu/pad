def solution():
    """Ernie's income is 4/5 of what it used to be and Jack's income is now twice what Ernie used to make. How much do they earn combined if Ernie used to make $6000?"""
    ernies_old_income = 6000
    ernies_new_income = ernies_old_income * (4/5)
    jacks_income = ernies_old_income * 2
    total_income = ernies_new_income + jacks_income
    result = total_income
    return result

print(solution())