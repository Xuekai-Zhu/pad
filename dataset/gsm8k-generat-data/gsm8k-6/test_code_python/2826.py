def solution():
    # Calculate the total amount paid by Sarah over 5 years
    total_paid = 5 * 12 * 600 + 10000  # 5 years of monthly payments plus the $10,000 down payment

    # Calculate the loan amount
    loan_amount = total_paid / 5
    result = loan_amount
    return result

print(solution())