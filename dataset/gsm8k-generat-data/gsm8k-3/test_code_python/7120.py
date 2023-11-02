def solution():
    """Adam's father deposited $2000 in the bank. It receives 8% interest paid throughout the year, and he withdraws the interest as soon as it is deposited.  How much will Adam’s father have, including his deposit and the interest received after 2 and a half years?"""
    # Set the initial deposit amount
    deposit = 2000

    # Calculate the interest earned after 2.5 years
    interest_rate = 0.08
    time_years = 2.5
    interest_earned = deposit * interest_rate * time_years

    # Calculate the total amount after the 2.5 years
    amount_total = deposit + interest_earned

    # Display the total amount
    result = amount_total
    return result

print(solution())