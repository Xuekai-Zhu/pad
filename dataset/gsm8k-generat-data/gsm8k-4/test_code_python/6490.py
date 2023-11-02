def solution():
    """Lucy has $65 in the bank. She made a $15 deposit and then followed by a $4 withdrawal. What is Lucy's bank balance?"""
    # Define the initial bank balance
    bank_balance = 65

    # Add the deposit to the bank balance
    bank_balance += 15

    # Subtract the withdrawal from the bank balance
    bank_balance -= 4

    # Return the final bank balance
    result = bank_balance
    return result

print(solution())