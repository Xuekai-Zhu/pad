def solution():
    amount_borrowed = 1200  # Jack borrowed $1200
    interest_rate = 0.1  # The interest rate is 10%
    interest_amount = amount_borrowed * interest_rate  # Calculate the interest amount
    total_amount = amount_borrowed + interest_amount  # Calculate the total amount to be paid back
    result = total_amount
    return result

print(solution())