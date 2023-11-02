def solution():
    total_budget = 32  # The town's annual budget is $32 million
    policing_budget = total_budget / 2  # Half of the budget goes towards policing
    education_budget = 12  # $12 million goes towards education

    # Calculate the remaining budget for managing public spaces
    remaining_budget = total_budget - policing_budget - education_budget
    result = remaining_budget
    return result

print(solution())