def solution():
    """Jerry owes a loan shark $200. The loan shark charges Jerry 10% interest compounded monthly. (This means that every month the loan shark adds Jerry's interest amount to his loan, and the next month Jerry has to pay 10% on the new total). If Jerry doesn't make any payments, how much (in dollars) does the loan shark charge in interest the second month?"""
    # Define the initial loan amount and interest rate
    loan_amount = 200
    interest_rate = 0.1

    # Calculate the interest charged in the first month
    interest_charged = loan_amount * interest_rate

    # Calculate the total amount owed after the first month
    total_amount_owed = loan_amount + interest_charged

    # Calculate the interest charged in the second month
    interest_charged_second_month = total_amount_owed * interest_rate

    # Return the result
    result = interest_charged_second_month
    return result

print(solution())