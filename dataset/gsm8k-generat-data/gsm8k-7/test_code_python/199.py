def solution():
    loan_amount = 6000
    num_years_to_repay = 2
    num_months_to_repay = num_years_to_repay * 12
    monthly_payment_2_years = loan_amount / num_months_to_repay

    num_years_to_repay = 5
    num_months_to_repay = num_years_to_repay * 12
    monthly_payment_5_years = loan_amount / num_months_to_repay

    extra_monthly_payment = monthly_payment_2_years - monthly_payment_5_years
    result = extra_monthly_payment
    return result

print(solution())