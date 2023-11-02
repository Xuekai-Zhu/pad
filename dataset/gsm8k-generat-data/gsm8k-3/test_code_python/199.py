def solution():
    """Gary bought his first used car for $6,000. Gary borrowed the money from his dad who said he could pay him back the full amount over 5 years. Gary decided he would pay his dad back the full amount in 2 years. How much more is Gary spending per month to pay the loan off in 2 years instead of 5?"""
    # Define the initial loan amount and the number of years to pay it
    INITIAL_LOAN = 6000
    INITIAL_YEARS = 5

    # Calculate the monthly payment for a 5-year loan
    monthly_payment_5years = INITIAL_LOAN / (INITIAL_YEARS * 12)

    # Define the new number of years to pay the loan
    NEW_YEARS = 2

    # Calculate the new monthly payment to pay off the loan in 2 years
    monthly_payment_2years = INITIAL_LOAN / (NEW_YEARS * 12)

    # Calculate the difference in monthly payments
    monthly_difference = monthly_payment_2years - monthly_payment_5years

    # return the result
    result = round(monthly_difference, 2)
    return result

print(solution())