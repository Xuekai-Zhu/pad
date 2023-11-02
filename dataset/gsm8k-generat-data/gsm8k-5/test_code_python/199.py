def solution():
    loan_amount = 6000  # Gary borrowed $6,000 from his dad
    repayment_period_1 = 5  # Gary's dad gave him 5 years to repay the loan
    repayment_period_2 = 2  # Gary decided to repay the loan in 2 years

    # Calculate the monthly payment for a 5-year repayment period
    monthly_payment_1 = loan_amount / (repayment_period_1 * 12)

    # Calculate the monthly payment for a 2-year repayment period
    monthly_payment_2 = loan_amount / (repayment_period_2 * 12)

    # Calculate the difference in monthly payment between the two repayment periods
    difference = monthly_payment_2 - monthly_payment_1
    result = difference
    return result

print(solution())