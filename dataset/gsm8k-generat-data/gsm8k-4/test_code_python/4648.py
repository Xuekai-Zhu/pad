def solution():
    """Vince owns a hair salon and he earns $18 per head. His monthly expenses are $280 for rent and electricity and 20% of his earnings are allocated for recreation and relaxation. He will save the rest. How much does he save if he serves 80 customers a month?"""
    # Define Vince's earnings per month
    earnings = 18 * 80

    # Define Vince's monthly expenses
    expenses = 280

    # Calculate Vince's recreation and relaxation expenses
    rr_expenses = earnings * 0.20

    # Calculate Vince's total expenses
    total_expenses = expenses + rr_expenses

    # Calculate Vince's savings
    savings = earnings - total_expenses

    # return the result
    result = savings
    return result

print(solution())