def solution():
    """The town’s annual budget totals $32 million. If half of the budget goes towards policing and $12 million goes towards education. How much money is left for managing public spaces?"""
    total_budget = 32
    policing_budget = total_budget / 2
    education_budget = 12
    public_spaces_budget = total_budget - (policing_budget + education_budget)
    result = public_spaces_budget
    return result

print(solution())