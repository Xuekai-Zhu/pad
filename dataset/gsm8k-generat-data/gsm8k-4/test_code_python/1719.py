def solution():
    """Tonya has $150.00 on her credit card. If she leaves any balance on her card at the end of the month, she is charged 20% interest. If she makes a $50.00 payment on her card, what will be the new balance?"""
    # Define the initial balance and the payment amount
    initial_balance = 150.00
    payment = 50.00

    # Calculate the remaining balance before interest
    balance_before_interest = initial_balance - payment

    # Apply interest if there is still a balance remaining
    if balance_before_interest > 0:
        balance_after_interest = balance_before_interest * 1.2
    else:
        balance_after_interest = 0

    # Return the new balance
    result = balance_after_interest
    return result

print(solution())