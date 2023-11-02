def solution():
    
    loan_amount = 100
    weeks = 2
    finance_fee = 0.05
    total_fees = 0
    
    for i in range(weeks):
        fees_this_week = loan_amount * finance_fee
        total_fees += fees_this_week
        finance_fee *= 2
        
    result = total_fees
    return result

print(solution())