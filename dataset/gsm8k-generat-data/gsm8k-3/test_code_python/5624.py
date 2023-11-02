def solution():
    """Jerry paid off some of his debts. Two months ago, he paid $12 while last month, he paid $3 more. If his debt was $50 in all, how much does he still have to pay?"""
    # Calculate the total amount Jerry paid in the first two months
    paid_first_two_months = 12 + (12 + 3)

    # Calculate how much Jerry still owes
    still_owes = 50 - paid_first_two_months

    # Display how much Jerry still owes
    result = still_owes
    return result

print(solution())