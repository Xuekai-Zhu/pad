def solution():
    """Steve puts $100 into the bank. Each year he earns 10% interest on the money in the account. How much money will be in the bank after 2 years?"""
    # Define the initial deposit and the interest rate
    initial_deposit = 100
    interest_rate = 0.1

    # Calculate the balance after the first year
    balance_year1 = initial_deposit * (1 + interest_rate)

    # Calculate the balance after the second year
    balance_year2 = balance_year1 * (1 + interest_rate)

    # return the result
    result = balance_year2
    return result

print(solution())