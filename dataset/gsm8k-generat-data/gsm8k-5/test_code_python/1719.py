def solution():
    original_balance = 150.00  # Tonya's original balance on her credit card
    payment = 50.00  # Tonya's payment on her card

    # Calculate the new balance if no interest is applied
    new_balance = original_balance - payment

    if new_balance > 0:
        # Apply 20% interest if there is a remaining balance
        interest = new_balance * 0.20
        new_balance += interest

    result = new_balance
    return result

print(solution())