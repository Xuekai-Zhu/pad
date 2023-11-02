def solution():
    # Define the initial loan amount and monthly interest rate
    loan_amount = 200
    monthly_interest_rate = 0.1 / 12

    # Calculate the interest charged after the first month
    interest_charged = loan_amount * monthly_interest_rate

    # Increase the loan amount by the interest charged
    new_loan_amount = loan_amount + interest_charged

    # Calculate the interest charged after the second month using the new loan amount
    interest_charged_second_month = new_loan_amount * monthly_interest_rate

    result = interest_charged_second_month
    return result

print(solution())