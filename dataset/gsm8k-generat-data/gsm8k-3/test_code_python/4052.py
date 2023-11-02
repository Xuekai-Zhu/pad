def solution():
    """Ernie's income is 4/5 of what it used to be and Jack's income is now twice what Ernie used to make. How much do they earn combined if Ernie used to make $6000?"""
    # Define Ernie's original income
    ernie_income_orig = 6000

    # Calculate Ernie's new income
    ernie_income_new = ernie_income_orig * (4/5)

    # Calculate Jack's income
    jack_income = ernie_income_orig * 2

    # Calculate the combined income
    combined_income = ernie_income_new + jack_income

    # Display the combined income
    result = combined_income
    return result

print(solution())