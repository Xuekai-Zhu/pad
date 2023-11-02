def solution():
    
    monthly_payment = 100
    loan_duration = 12
    loan_amount = monthly_payment * loan_duration
    interest_rate = 0.1
    interest_fee = loan_amount * interest_rate
    total_owed = loan_amount + interest_fee
    result = total_owed
    return result

print(solution())