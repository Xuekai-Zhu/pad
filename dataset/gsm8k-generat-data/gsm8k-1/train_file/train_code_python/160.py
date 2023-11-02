def solution():
    """The town’s annual budget totals $32 million. If half of the budget goes towards policing and $12 million goes towards education. How much money is left for managing public spaces?"""
    budget = 32000000
    policing_budget = budget / 2
    education_budget = 12000000
    public_spaces_budget = budget - policing_budget - education_budget
    result = public_spaces_budget
    return result

print(solution())