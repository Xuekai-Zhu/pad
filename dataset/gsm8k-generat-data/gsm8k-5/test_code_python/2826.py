def solution():
    total_months = 5 * 12  # Sarah has 5 years, or 60 months, to pay back the loan
    down_payment = 10000  # Sarah put $10,000 down as a down payment
    monthly_payment = 600  # Sarah's monthly payments are $600.00

    # Calculate the total amount Sarah will pay back in monthly payments
    total_payments = total_months * monthly_payment

    # Add the down payment to the total payments to find the total loan amount
    total_loan = down_payment + total_payments
    result = total_loan
    return result

print(solution())