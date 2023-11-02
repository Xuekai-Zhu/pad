def solution():
    car_cost = 32000  # cost of the car
    down_payment = 8000  # down payment
    loan_amount = car_cost - down_payment  # amount needed for loan
    num_payments = 48  # number of monthly payments
    interest_rate = 5/100  # interest rate per month

    # Calculate the monthly payments needed for the loan, including interest
    monthly_interest = loan_amount * interest_rate
    monthly_payment = (loan_amount + monthly_interest) / num_payments

    result = monthly_payment
    return result

print(solution())