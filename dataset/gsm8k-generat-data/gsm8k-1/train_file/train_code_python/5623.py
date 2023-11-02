def solution():
    """Jerry paid off some of his debts. Two months ago, he paid $12 while last month, he paid $3 more. If his debt was $50 in all, how much does he still have to pay?"""
    total_debt = 50
    payment_1 = 12
    payment_2 = 15
    amount_paid = payment_1 + payment_2
    amount_remaining = total_debt - amount_paid
    result = amount_remaining
    return result

print(solution())