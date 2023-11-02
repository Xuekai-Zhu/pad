def solution():
    loan_amount = 10000
    down_payment = 1000
    monthly_payment = 600
    months = 60
    total_payment = monthly_payment * months
    result = total_payment + down_payment
    
    return result

print(solution())