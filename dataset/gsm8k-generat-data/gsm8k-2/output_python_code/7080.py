def solution():
    """A teacher purchased some school supplies that cost $13 and $24. She had the remaining $6 budget from last year and for this year, she was given a $50 budget. How much money remains in her budget after purchasing the school supplies?"""
    initial_budget = 6 + 50
    cost = 13 + 24
    remaining_budget = initial_budget - cost
    result = remaining_budget
    return result

print(solution())