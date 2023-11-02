def solution():
    # Calculate the monthly payment if the loan is paid off over 5 years
    monthly_payment_5_years = 6000 / (5 * 12)  

    # Calculate the monthly payment if the loan is paid off over 2 years
    monthly_payment_2_years = 6000 / (2 * 12)  

    # Calculate the difference in monthly payments
    difference = monthly_payment_2_years - monthly_payment_5_years
    result = difference
    return result

print(solution())