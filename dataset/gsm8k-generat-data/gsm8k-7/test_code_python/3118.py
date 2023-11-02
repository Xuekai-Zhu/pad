def solution():
    car_cost = 32000
    down_payment = 8000
    loan_amount = car_cost - down_payment
    num_payments = 48
    interest_rate = 0.05

    # Calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate the monthly payment without factoring in interest
    monthly_payment_before_interest = loan_amount / num_payments

    # Calculate the monthly payment with interest added
    monthly_payment = monthly_payment_before_interest + (monthly_interest_rate * loan_amount)

    result = monthly_payment
    return result

print(solution())