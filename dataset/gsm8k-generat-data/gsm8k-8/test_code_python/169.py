def solution():
    # Define the amount of grapes used per 6 months
    grapes_per_6_months = 90

    # Calculate the amount of grapes used per year
    grapes_per_year = 2 * grapes_per_6_months

    # Calculate the amount of grapes needed after increasing production by 20%
    increased_grapes_per_year = grapes_per_year * 1.2

    result = increased_grapes_per_year
    return result

print(solution())