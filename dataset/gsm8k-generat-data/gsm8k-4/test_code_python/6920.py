def solution():
    """A person puts $5600 in a bank for two years. Each year he earns interest of 7% of the original amount deposited. How much will this person have in the bank after two years?"""
    # Define the initial deposit and interest rate
    initial_deposit = 5600
    interest_rate = 0.07

    # Calculate the amount after the first year
    year_one_amount = initial_deposit + initial_deposit * interest_rate

    # Calculate the amount after the second year
    year_two_amount = year_one_amount + year_one_amount * interest_rate

    # Return the final amount
    result = year_two_amount
    return result

print(solution())