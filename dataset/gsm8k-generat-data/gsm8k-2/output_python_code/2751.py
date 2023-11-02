def solution():
    """The town of Centerville spends 15% of its annual budget on its public library. Centerville spent $3,000 on its public library and 24% on the public parks. How much is left of the annual budget?"""
    library_percentage = 15
    park_percentage = 24
    library_spending = 3000
    total_percentage_spent = library_percentage + park_percentage
    remaining_percentage = 100 - total_percentage_spent
    remaining_budget = (remaining_percentage / 100) * library_spending
    result = remaining_budget
    return result

print(solution())