def solution():
    """Jerry paid off some of his debts. Two months ago, he paid $12 while last month, he paid $3 more. If his debt was $50 in all, how much does he still have to pay?"""
    # Define the total debt and the amount already paid
    total_debt = 50
    amount_paid = 12 + 15  # last month's payment was $3 more than the previous month's

    # Calculate the amount still owed
    amount_owed = total_debt - amount_paid

    result = amount_owed
    return result

print(solution())