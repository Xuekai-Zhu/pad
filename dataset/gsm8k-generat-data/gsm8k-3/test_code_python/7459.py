def solution():
    """Mathilda is determined to pay back the money she owes a friend so she decides to pay an initial installment of $125. If she still has 75% left to pay, how much did she owe originally?"""
    # Define the initial payment and the remaining percentage left to pay
    initial_payment = 125
    remaining_percent = 75

    # Calculate the original amount owed
    original_amount = initial_payment / (1 - remaining_percent/100)

    # Display the original amount owed
    result = original_amount
    return result

print(solution())