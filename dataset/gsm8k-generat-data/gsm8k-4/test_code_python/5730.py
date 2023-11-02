def solution():
    """Chip has a $50.00 balance on his credit card. Since he didn't pay it off, he will be charged a 20% interest fee. He puts $20.00 on his credit card the following month and doesn't make any payments to his debt. He is hit with another 20% interest fee. What's the current balance on his credit card?"""
    # Define the initial balance and interest rate
    balance = 50.0
    interest_rate = 0.2

    # Calculate the interest and new balance for the first month
    interest = balance * interest_rate
    balance += interest + 20.0

    # Calculate the interest and new balance for the second month
    interest = balance * interest_rate
    balance += interest

    # return the result
    result = round(balance, 2)
    return result

print(solution())