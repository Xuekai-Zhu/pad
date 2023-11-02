def solution():
    # Define the original loan amount and the number of years to pay it back
    original_loan = 6000
    original_years = 5

    # Calculate the monthly payment for the original loan
    original_monthly_payment = original_loan / (original_years * 12)

    # Define the new number of years to pay back the loan
    new_years = 2

    # Calculate the total amount to pay back the loan in 2 years
    new_total_payment = original_loan / new_years

    # Calculate the monthly payment for the new payment plan
    new_monthly_payment = new_total_payment / (new_years * 12)

    # Calculate the difference in monthly payments
    monthly_payment_diff = new_monthly_payment - original_monthly_payment

    result = monthly_payment_diff
    return result

print(solution())