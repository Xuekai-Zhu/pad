def solution():
    
    down_payment = 10000
    monthly_payment = 600
    number_of_payments = 60
    total_amount_paid = down_payment + (monthly_payment * number_of_payments)
    loan_amount = total_amount_paid
    result = loan_amount
    
    return result

print(solution())