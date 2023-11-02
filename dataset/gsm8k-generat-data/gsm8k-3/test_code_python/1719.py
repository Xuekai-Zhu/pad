def solution():
    """Tonya has $150.00 on her credit card.  If she leaves any balance on her card at the end of the month, she is charged 20% interest.  If she makes a $50.00 payment on her card, what will be the new balance?"""
    # Define Tonya's initial balance and the interest rate
    initial_balance = 150.00
    interest_rate = 0.20

    # Subtract Tonya's payment from her initial balance
    remaining_balance = initial_balance - 50.00

    # Calculate Tonya's new balance with interest if she doesn't pay off the full amount
    if remaining_balance > 0:
        new_balance = remaining_balance + (remaining_balance * interest_rate)
    else:
        new_balance = 0

    # Display Tonya's new balance
    result = new_balance
    return result

print(solution())