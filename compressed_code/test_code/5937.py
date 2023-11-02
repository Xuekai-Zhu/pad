def solution():
    
    loan_amount = 6000
    repayment_duration_1 = 5
    repayment_duration_2 = 2
    monthly_repayment_1 = loan_amount / (repayment_duration_1 * 12)
    monthly_repayment_2 = loan_amount / (repayment_duration_2 * 12)
    difference = monthly_repayment_2 - monthly_repayment_1
    result = difference
    return result

print(solution())