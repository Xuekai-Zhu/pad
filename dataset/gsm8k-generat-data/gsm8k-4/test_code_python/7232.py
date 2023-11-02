def solution():
    """Emma has saved $230 in her bank account. She withdrew $60 to buy a new pair of shoes. The next week, she deposited twice as much money as she withdrew. How much is in her bank account now?"""
    # Define initial amount and withdrawal/deposit amounts
    initial_amount = 230
    withdrawal_amount = 60
    deposit_amount = withdrawal_amount * 2

    # Calculate the new amount after the withdrawal and deposit
    new_amount = initial_amount - withdrawal_amount + deposit_amount

    result = new_amount
    return result

print(solution())