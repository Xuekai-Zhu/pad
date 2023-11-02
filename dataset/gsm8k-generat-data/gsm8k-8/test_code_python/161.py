def solution():
    # Calculate the amount of the budget that goes towards policing
    policing_budget = 0.5 * 32000000

    # Calculate the amount of the budget that goes towards education
    education_budget = 12000000

    # Calculate the amount of the budget left for managing public spaces
    public_spaces_budget = 32000000 - policing_budget - education_budget
    result = public_spaces_budget
    return result

print(solution())