def solution():
    """Ernie's income is 4/5 of what it used to be and Jack's income is now twice what Ernie used to make. How much do they earn combined if Ernie used to make $6000?"""
    # Define Ernie's original income
    ernie_income = 6000

    # Calculate Ernie's current income
    ernie_new_income = ernie_income * 4/5

    # Calculate Jack's current income
    jack_income = ernie_income * 2

    # Calculate the combined income of Ernie and Jack
    combined_income = ernie_new_income + jack_income

    # return the result
    result = combined_income
    return result

print(solution())