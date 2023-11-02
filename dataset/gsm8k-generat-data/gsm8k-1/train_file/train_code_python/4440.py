def solution():
    """Two months ago, Wilson had a total of $150 in his bank account. Then last month, he deposited $17. A few days after, he made a withdrawal. This month, he deposited $21 so he has $16 more than what is in his account two months ago. How much did Wilson withdraw last month?"""
    starting_balance = 150
    last_month_deposit = 17
    this_month_deposit = 21
    current_balance = starting_balance + last_month_deposit - withdraw_amount + this_month_deposit
    withdraw_amount = current_balance - starting_balance - 16
    result = withdraw_amount
    return result

print(solution())