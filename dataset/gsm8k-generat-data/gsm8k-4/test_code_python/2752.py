def solution():
    """The town of Centerville spends 15% of its annual budget on its public library. Centerville spent $3,000 on its public library and 24% on the public parks. How much is left of the annual budget?"""
    # Define the amount spent on the public library and the percentage of the budget spent on it
    library_spending = 3000
    library_percentage = 0.15

    # Calculate the total annual budget
    total_budget = library_spending / library_percentage

    # Calculate the amount spent on public parks
    parks_spending = total_budget * 0.24

    # Calculate the amount left in the annual budget
    remaining_budget = total_budget - library_spending - parks_spending

    # return the result
    result = remaining_budget
    return result

print(solution())