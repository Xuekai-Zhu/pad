def solution():
    monthly_payment = 100.0
    num_months = 12
    loan_amount = monthly_payment * num_months

    interest_rate = 0.1  # 10% interest fee
    interest_amount = loan_amount * interest_rate

    total_amount_due = loan_amount + interest_amount
    result = total_amount_due
    return result

print(solution())