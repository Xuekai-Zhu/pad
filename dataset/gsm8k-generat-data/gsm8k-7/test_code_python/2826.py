def solution():
    down_payment = 10000
    monthly_payment = 600
    loan_years = 5
    num_payments = loan_years * 12

    # Calculate the total amount of money paid for monthly payments
    total_monthly_payments = num_payments * monthly_payment

    # Calculate the loan amount by adding the total payments to the down payment
    loan_amount = total_monthly_payments + down_payment
    result = loan_amount
    return result

print(solution())