def solution():
    friday_spending = x
    saturday_spending = 2 * x
    sunday_spending = 3 * x

    total_spending = friday_spending + saturday_spending + sunday_spending

    if total_spending == 120:
        result = x
    else:
        result = "Cannot determine the value of X"

    return result

print(solution())