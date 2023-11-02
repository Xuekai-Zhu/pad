def solution():
    """Emma has saved $230 in her bank account. She withdrew $60 to buy a new pair of shoes. The next week, she deposited twice as much money as she withdrew. How much is in her bank account now?"""
    # Define Emma's initial savings and withdrawal amount
    initial_savings = 230
    withdrawal = 60

    # Calculate Emma's remaining balance after the withdrawal
    remaining_balance = initial_savings - withdrawal

    # Calculate Emma's deposit amount
    deposit = withdrawal * 2

    # Calculate Emma's final balance after the deposit
    final_balance = remaining_balance + deposit

    # Display Emma's final balance
    result = final_balance
    return result

print(solution())