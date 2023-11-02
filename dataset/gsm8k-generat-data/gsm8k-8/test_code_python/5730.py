def solution():
    # Define the initial balance and interest rate
    balance = 50.00
    interest_rate = 0.20

    # Calculate the first month balance with interest and new purchase
    month1_balance = balance + (balance * interest_rate) + 20.00

    # Calculate the second month balance with interest
    month2_balance = month1_balance + (month1_balance * interest_rate)

    result = month2_balance
    return result

print(solution())