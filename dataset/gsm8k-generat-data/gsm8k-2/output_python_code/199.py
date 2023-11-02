def solution():
    """Gary bought his first used car for $6,000. Gary borrowed the money from his dad who said he could pay him back the full amount over 5 years. Gary decided he would pay his dad back the full amount in 2 years. How much more is Gary spending per month to pay the loan off in 2 years instead of 5?"""
    loan_amount = 6000
    years_5_interest = 0.05
    years_2_interest = 0.08
    
    # Calculate total interest paid over 5 years
    total_interest_5_years = loan_amount * years_5_interest * 5
    
    # Calculate total interest paid over 2 years
    total_interest_2_years = loan_amount * years_2_interest * 2
    
    # Calculate monthly payments for 5 years
    monthly_payments_5_years = (loan_amount + total_interest_5_years) / (5 * 12)
    
    # Calculate monthly payments for 2 years
    monthly_payments_2_years = (loan_amount + total_interest_2_years) / (2 * 12)
    
    # Calculate difference in monthly payments
    monthly_payment_difference = monthly_payments_2_years - monthly_payments_5_years
    
    result = monthly_payment_difference
    return result

print(solution())