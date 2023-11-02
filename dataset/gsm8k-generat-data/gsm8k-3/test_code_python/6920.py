def solution():
    """A person puts $5600 in a bank for two years. Each year he earns interest of 7% of the original amount deposited. How much will this person have in the bank after two years?"""
    # Define the initial deposit and interest rate
    INITIAL_DEPOSIT = 5600
    INTEREST_RATE = 0.07

    # Calculate the interest earned in the first year
    interest_1 = INITIAL_DEPOSIT * INTEREST_RATE

    # Calculate the balance after the first year
    balance_1 = INITIAL_DEPOSIT + interest_1

    # Calculate the interest earned in the second year
    interest_2 = balance_1 * INTEREST_RATE

    # Calculate the final balance after two years
    final_balance = balance_1 + interest_2

    # Display the final balance
    result = final_balance
    return result

print(solution())