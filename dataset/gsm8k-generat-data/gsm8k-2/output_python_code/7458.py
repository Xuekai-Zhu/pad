def solution():
    """Mathilda is determined to pay back the money she owes a friend so she decides to pay an initial installment of $125. If she still has 75% left to pay, how much did she owe originally?"""
    initial_payment = 125
    remaining_debt_percent = 0.75
    remaining_debt = initial_payment / (1 - remaining_debt_percent)
    original_debt = remaining_debt + initial_payment
    result = original_debt
    return result

print(solution())