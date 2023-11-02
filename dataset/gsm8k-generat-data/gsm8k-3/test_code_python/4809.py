def solution():
    """Jerry owes a loan shark $200. The loan shark charges Jerry 10% interest compounded monthly. (This means that every month the loan shark adds Jerry's interest amount to his loan, and the next month Jerry has to pay 10% on the new total). If Jerry doesn't make any payments, how much (in dollars) does the loan shark charge in interest the second month?"""
    # Define the initial loan amount and interest rate
    loan_amount = 200
    interest_rate = 0.1

    # Calculate the interest charged in the first month
    interest_1 = loan_amount * interest_rate

    # Calculate the new loan balance after the first month
    new_balance = loan_amount + interest_1

    # Calculate the interest charged in the second month using the new balance as the loan amount
    interest_2 = new_balance * interest_rate

    # Display the interest charged in the second month
    result = interest_2
    return result

print(solution())