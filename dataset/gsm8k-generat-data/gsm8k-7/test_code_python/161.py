def solution():
    total_budget = 32  # in millions
    police_budget = total_budget / 2
    education_budget = 12

    # Calculate the budget for managing public spaces
    public_spaces_budget = total_budget - (police_budget + education_budget)
    result = public_spaces_budget
    return result

print(solution())