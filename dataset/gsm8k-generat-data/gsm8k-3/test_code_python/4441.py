def solution():
    """Two months ago, Wilson had a total of $150 in his bank account. Then last month, he deposited $17. A few days after, he made a withdrawal. This month, he deposited $21 so he has $16 more than what is in his account two months ago. How much did Wilson withdraw last month?"""
    # Define the initial balance two months ago
    initial_balance = 150

    # Define the deposits and withdrawals
    deposit_1 = 17
    withdrawal_1 = None # Define as None for now
    deposit_2 = 21

    # Calculate the final balance
    final_balance = initial_balance + deposit_1 - withdrawal_1 + deposit_2

    # Calculate the balance two months ago + $16
    target_balance = initial_balance + 16

    # Calculate the withdrawal amount
    withdrawal_1 = initial_balance + deposit_1 + deposit_2 - target_balance

    # Display the withdrawal amount
    result = withdrawal_1
    return result

print(solution())