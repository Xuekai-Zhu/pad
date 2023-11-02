def solution():
    """Karan borrowed $3,650 for five months at an interest rate of 10%. She has to pay an equal amount every month. How much does she have to pay per month?"""
    principal = 3650
    interest_rate = 0.1
    time_in_months = 5
    total_interest = principal * interest_rate * time_in_months
    total_amount_due = principal + total_interest
    monthly_payment = total_amount_due / time_in_months
    result = monthly_payment
    return result

print(solution())