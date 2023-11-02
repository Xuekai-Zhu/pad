def solution():
    interest_rate = 0.12  # The interest rate is 12%
    total_interest = 1500  # The total interest is $1500

    # Calculate the borrowed amount using the formula I = P * R * T, where I is the total interest, 
    # P is the borrowed amount, R is the interest rate, and T is the time (in years)
    borrowed_amount = total_interest / (interest_rate * 1)

    result = borrowed_amount
    return result

print(solution())