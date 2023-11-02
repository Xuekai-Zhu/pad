def solution():
    
    house_cost = 480000
    trailer_cost = 120000
    loan_years = 20
    loan_months = loan_years * 12
    house_payment = house_cost / loan_months
    trailer_payment = trailer_cost / loan_months
    monthly_difference = house_payment - trailer_payment
    result = monthly_difference
    return result

print(solution())