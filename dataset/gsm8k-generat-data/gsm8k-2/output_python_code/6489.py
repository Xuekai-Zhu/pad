def solution():
    """Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. What is Lucy's bank balance?"""
    starting_balance = 65
    deposit = 15
    withdrawal = 4
    current_balance = starting_balance + deposit - withdrawal
    result = current_balance
    return result

print(solution())