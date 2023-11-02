def solution():
    
    loan_amount = 100 * 12
    interest_rate = 0.1
    interest_fee = loan_amount * interest_rate
    total_amount = loan_amount + interest_fee
    result = total_amount
    return result

print(solution())