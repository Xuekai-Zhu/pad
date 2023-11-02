def solution():
    # Calculate Wilson's current account balance
    current_balance = 150 + 17 + 21 + 16  # last month's deposit + this month's deposit + additional $16 in the account
    # Calculate Wilson's account balance before the withdrawals
    previous_balance = current_balance - withdrawal
    # Calculate the withdrawal amount
    withdrawal = previous_balance - (150 + 17)
    result = withdrawal
    return result

print(solution())