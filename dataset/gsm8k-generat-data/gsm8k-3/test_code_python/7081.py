def solution():
    """A teacher purchased some school supplies that cost $13 and $24. She had the remaining $6 budget from last year and for this year, she was given a $50 budget. How much money remains in her budget after purchasing the school supplies?"""
    # Define the cost of the school supplies
    SUPPLY_COST = 13 + 24

    # Define the initial budget
    INITIAL_BUDGET = 6 + 50

    # Calculate the remaining budget after purchasing the supplies
    remaining_budget = INITIAL_BUDGET - SUPPLY_COST

    # Display the remaining budget
    result = remaining_budget
    return result

print(solution())