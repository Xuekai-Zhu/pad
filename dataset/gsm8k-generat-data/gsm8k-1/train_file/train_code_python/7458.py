def solution():
    """Mathilda is determined to pay back the money she owes a friend so she decides to pay an initial installment of $125. If she still has 75% left to pay, how much did she owe originally?"""
    initial_payment = 125
    remaining_balance_percent = 75
    remaining_balance_decimal = remaining_balance_percent / 100
    total_balance = initial_payment / (1 - remaining_balance_decimal)
    result = total_balance
    return result

print(solution())