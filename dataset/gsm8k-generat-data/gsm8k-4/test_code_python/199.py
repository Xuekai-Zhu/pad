def solution():
    """Gary bought his first used car for $6,000. Gary borrowed the money from his dad who said he could pay him back the full amount over 5 years. Gary decided he would pay his dad back the full amount in 2 years. How much more is Gary spending per month to pay the loan off in 2 years instead of 5?"""
    # Define the initial loan amount, the number of years to pay it off, and the interest rate
    loan_amount = 6000
    years_5 = 5
    years_2 = 2

    # Calculate the monthly payment required to pay off the loan in 5 years
    monthly_payment_5 = loan_amount / (years_5 * 12)

    # Calculate the monthly payment required to pay off the loan in 2 years
    monthly_payment_2 = loan_amount / (years_2 * 12)

    # Calculate the difference in monthly payments
    monthly_payment_diff = monthly_payment_2 - monthly_payment_5

    # Return the result
    result = round(monthly_payment_diff, 2)
    return result

print(solution())