def solution():
    """Steve puts $100 into the bank. Each year he earns 10% interest on the money in the account. How much money will be in the bank after 2 years?"""
    # Define the initial amount and interest rate
    initial_amount = 100
    interest_rate = 0.1

    # Calculate the amount in the bank after 2 years
    total_amount = initial_amount * (1 + interest_rate)**2

    # Display the total amount in the bank after 2 years
    result = total_amount
    return result

print(solution())