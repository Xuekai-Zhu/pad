def solution():
    """Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. What is Lucy's bank balance?"""
    balance = 65
    deposit = 15
    withdrawal = 4
    new_balance = balance + deposit - withdrawal
    result = new_balance
    return result

print(solution())