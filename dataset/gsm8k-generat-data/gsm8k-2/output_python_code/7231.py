def solution():
    """Emma has saved $230 in her bank account. She withdrew $60 to buy a new pair of shoes. The next week, she deposited twice as much money as she withdrew. How much is in her bank account now?"""
    initial_balance = 230
    withdraw_amount = 60
    deposit_amount = 2 * withdraw_amount
    new_balance = initial_balance - withdraw_amount + deposit_amount
    result = new_balance
    return result

print(solution())