def solution():
    """Chip has a $50.00 balance on his credit card.  Since he didn't pay it off, he will be charged a 20% interest fee. 
    He puts $20.00 on his credit card the following month and doesn't make any payments to his debt.  
    He is hit with another 20% interest fee.  What's the current balance on his credit card?"""
    # Define Chip's starting balance and the interest rate
    starting_balance = 50
    interest_rate = 0.2

    # Calculate the interest charged for the first month
    interest_1 = starting_balance * interest_rate

    # Calculate Chip's balance after the first month
    balance_1 = starting_balance + interest_1

    # Add Chip's monthly charge to his balance
    balance_2 = balance_1 + 20

    # Calculate the interest charged for the second month
    interest_2 = balance_2 * interest_rate

    # Calculate Chip's balance after the second month
    balance_3 = balance_2 + interest_2

    # Display Chip's current balance
    result = balance_3
    return result

print(solution())