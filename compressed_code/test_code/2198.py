def solution():
    
    down_payment = 10000
    monthly_payment = 600
    loan_length_months = 5 * 12
    total_payments = loan_length_months * monthly_payment
    loan_amount = down_payment + total_payments
    result = loan_amount
    return result

print(solution())