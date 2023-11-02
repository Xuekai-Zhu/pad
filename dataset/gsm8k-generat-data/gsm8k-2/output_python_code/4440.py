def solution():
    """Two months ago, Wilson had a total of $150 in his bank account. Then last month, he deposited $17. A few days after, he made a withdrawal. This month, he deposited $21 so he has $16 more than what is in his account two months ago. How much did Wilson withdraw last month?"""
    initial_balance = 150
    last_month_deposit = 17
    current_balance = initial_balance + last_month_deposit
    current_balance_with_extra = initial_balance + 16
    withdrawn_amount = current_balance - current_balance_with_extra - 21
    result = withdrawn_amount
    return result

print(solution())