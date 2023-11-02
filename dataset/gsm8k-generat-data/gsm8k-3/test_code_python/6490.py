def solution():
    """Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. What is Lucy's bank balance?"""
    # Define Lucy's initial bank balance
    initial_balance = 65

    # Calculate Lucy's new balance after the deposit
    balance_after_deposit = initial_balance + 15

    # Calculate Lucy's final balance after the withdrawal
    final_balance = balance_after_deposit - 4

    # Display Lucy's final balance
    result = final_balance
    return result

print(solution())