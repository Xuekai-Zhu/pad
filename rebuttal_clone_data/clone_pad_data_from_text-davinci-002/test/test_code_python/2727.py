def solution():
    loan_amount = 200
    interest_rate = 10
    interest_charged = loan_amount * (interest_rate/100)
    new_loan_amount = loan_amount + interest_charged
    second_month_interest = new_loan_amount * (interest_rate/100)
    result = second_month_interest
    
    return result

print(solution())