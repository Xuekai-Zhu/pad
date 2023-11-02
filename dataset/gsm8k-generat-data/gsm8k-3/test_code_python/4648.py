def solution():
    """Vince owns a hair salon and he earns $18 per head. His monthly expenses are $280 for rent and electricity and 20% of his earnings are allocated for recreation and relaxation. He will save the rest. How much does he save if he serves 80 customers a month?"""
    # Define the cost per head and monthly expenses
    COST_PER_HEAD = 18
    MONTHLY_EXPENSES = 280

    # Define the number of customers served
    customers = 80

    # Calculate the total earnings
    earnings = customers * COST_PER_HEAD

    # Calculate the expenses and remaining earnings
    expenses = MONTHLY_EXPENSES + (earnings * 0.2)
    remaining_earnings = earnings - expenses

    # Display the amount that Vince saves
    result = remaining_earnings
    return result

print(solution())