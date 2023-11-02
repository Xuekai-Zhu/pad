def solution():
    """The town’s annual budget totals $32 million. If half of the budget goes towards policing and $12 million goes towards education. How much money is left for managing public spaces?"""
    # Define the total budget and the amount spent on policing and education
    total_budget = 32000000
    policing_budget = total_budget / 2
    education_budget = 12000000

    # Calculate the amount of money left for managing public spaces
    public_spaces_budget = total_budget - policing_budget - education_budget

    # return the result
    result = public_spaces_budget
    return result

print(solution())