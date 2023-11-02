def solution():
    # Calculate the amount of money spent on policing and education
    police_budget = 0.5 * 32
    education_budget = 12

    # Calculate the amount of money left for managing public spaces
    public_spaces_budget = 32 - police_budget - education_budget
    result = public_spaces_budget
    return result

print(solution())