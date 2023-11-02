def solution():
    car_cost = 32000  # The car costs $32,000
    down_payment = 8000  # Jason makes a down payment of $8,000
    loan_amount = car_cost - down_payment  # Jason needs a loan for the rest of the amount
    num_payments = 48  # Jason has to make 48 equal monthly payments
    interest_rate = 0.05  # Jason pays interest equal to 5% of that month's payment

    # Calculate the monthly payment
    monthly_interest_rate = interest_rate / 12
    numerator = (loan_amount * monthly_interest_rate) * ((1 + monthly_interest_rate) ** num_payments)
    denominator = ((1 + monthly_interest_rate) ** num_payments) - 1
    monthly_payment = numerator / denominator
    result = monthly_payment
    return result

print(solution())