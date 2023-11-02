def solution():
    """Jerry paid off some of his debts. Two months ago, he paid $12 while last month, he paid $3 more. If his debt was $50 in all, how much does he still have to pay?"""
    total_debt = 50
    first_payment = 12
    second_payment = first_payment + 3
    paid_off = first_payment + second_payment
    remaining_debt = total_debt - paid_off
    result = remaining_debt
    return result

print(solution())