def solution():
    # Define the borrowed amount and interest rate
    borrowed_amount = 1200
    interest_rate = 0.1

    # Calculate the interest on the borrowed amount
    interest = borrowed_amount * interest_rate

    # Add the interest to the borrowed amount to get the total amount paid back
    total_paid_back = borrowed_amount + interest

    result = total_paid_back
    return result

print(solution())