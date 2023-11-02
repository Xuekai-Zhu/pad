def solution():
    """Mathilda is determined to pay back the money she owes a friend so she decides to pay an initial installment of $125. If she still has 75% left to pay, how much did she owe originally?"""
    # Define the initial installment and remaining balance
    initial_installment = 125
    remaining_balance_percentage = 0.75

    # Calculate the original balance
    original_balance = initial_installment / (1 - remaining_balance_percentage)

    # return the result
    result = round(original_balance)
    return result

print(solution())