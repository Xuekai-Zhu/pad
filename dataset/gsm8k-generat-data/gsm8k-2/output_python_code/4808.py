def solution():
    """Jerry owes a loan shark $200. The loan shark charges Jerry 10% interest compounded monthly.
    (This means that every month the loan shark adds Jerry's interest amount to his loan, 
    and the next month Jerry has to pay 10% on the new total).
    If Jerry doesn't make any payments, how much (in dollars) does the loan shark charge in interest the second month?"""
    loan_amount = 200
    annual_interest_rate = 0.1
    monthly_interest_rate = annual_interest_rate / 12
    first_month_interest = loan_amount * monthly_interest_rate
    second_month_loan_amount = loan_amount + first_month_interest
    second_month_interest = second_month_loan_amount * monthly_interest_rate
    result = second_month_interest
    return result

print(solution())