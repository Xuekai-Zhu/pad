def solution():
    """Adam's father deposited $2000 in the bank. It receives 8% interest paid throughout the year, and he withdraws the interest as soon as it is deposited. How much will Adam’s father have, including his deposit and the interest received after 2 and a half years?"""
    # Define the initial deposit and interest rate
    initial_deposit = 2000
    interest_rate = 0.08

    # Calculate the total interest earned after 2.5 years
    time_in_years = 2.5
    total_interest = initial_deposit * interest_rate * time_in_years

    # Calculate the final balance, including the initial deposit and earned interest
    final_balance = initial_deposit + total_interest

    # Round the final balance to 2 decimal places
    result = round(final_balance, 2)
    return result

print(solution())