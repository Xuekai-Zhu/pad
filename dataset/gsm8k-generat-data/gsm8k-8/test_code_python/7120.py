def solution():
    # Define the initial deposit amount and interest rate
    deposit_amount = 2000
    interest_rate = 0.08

    # Calculate the interest earned after 2.5 years
    interest_earned = deposit_amount * interest_rate * 2.5

    # Add the interest earned to the initial deposit amount
    total_amount = deposit_amount + interest_earned

    result = total_amount
    return result

print(solution())