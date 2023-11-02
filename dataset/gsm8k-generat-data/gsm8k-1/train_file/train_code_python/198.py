def solution():
    """Gary bought his first used car for $6,000. Gary borrowed the money from his dad who said he could pay him back the full amount over 5 years. Gary decided he would pay his dad back the full amount in 2 years. How much more is Gary spending per month to pay the loan off in 2 years instead of 5?"""
    loan_amount = 6000
    repayment_duration_1 = 5
    repayment_duration_2 = 2
    monthly_repayment_1 = loan_amount / (repayment_duration_1 * 12)
    monthly_repayment_2 = loan_amount / (repayment_duration_2 * 12)
    difference = monthly_repayment_2 - monthly_repayment_1
    result = difference
    return result

print(solution())