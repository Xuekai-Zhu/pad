def solution():
    """Jerry owes a loan shark $200. The loan shark charges Jerry 10% interest compounded monthly. (This means that every month the loan shark adds Jerry's interest amount to his loan, and the next month Jerry has to pay 10% on the new total). If Jerry doesn't make any payments, how much (in dollars) does the loan shark charge in interest the second month?"""
    initial_loan = 200
    interest_rate = 0.10
    months = 2
    compounded_loan = initial_loan * pow(1 + interest_rate, months)
    interest_charged = compounded_loan - initial_loan
    result = interest_charged
    return result

print(solution())