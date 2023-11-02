def solution():
    """Yasmin deposited a $50 birthday check from her grandmother in her bank account. The check was worth a quarter of her new balance after the check money is added. How many dollars were in her account before she deposited the check?"""
    check_amount = 50
    multiplier = 1 / (1 - 0.25)
    balance_after_check = check_amount * multiplier
    balance_before_check = balance_after_check - check_amount
    result = balance_before_check
    return result

print(solution())