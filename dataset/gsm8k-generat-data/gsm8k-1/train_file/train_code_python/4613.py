def solution():
    """Yasmin deposited a $50 birthday check from her grandmother in her bank account. The check was worth a quarter of her new balance after the check money is added. How many dollars were in her account before she deposited the check?"""
    check_amount = 50
    balance_after_check = check_amount / 0.25
    initial_balance = balance_after_check - check_amount
    result = initial_balance
    return result

print(solution())