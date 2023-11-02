def solution():
    borrowed_amount = 3650  # Karan borrowed $3,650
    interest_rate = 0.1  # Karan's interest rate is 10%
    num_months = 5  # Karan has to pay for 5 months

    # Calculate the interest rate
    interest_rate = borrowed_amount * interest_rate

    # Calculate the amount Karan needs to pay per month
    monthly_payment = borrowed_amount / num_months
    result = monthly_payment
    return result

print(solution())