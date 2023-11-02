def solution():
    ernie_income = 4/5 * 6000  # Ernie's income is 4/5 of what he used to make, which is $6000
    jack_income = 2 * (6000 - ernie_income)  # Jack's income is twice what Ernie used to make, after Ernie's income decreased by 20%

    # Calculate the combined income of Ernie and Jack
    combined_income = ernie_income + jack_income
    result = combined_income
    return result

print(solution())