def solution():
    
    student_payment = 300
    credit_card_minimum = 200
    mortgage_minimum = 500
    annual_minimum = student_payment + credit_card_minimum + mortgage_minimum
    monthly_increase = 0.5
    monthly_increase = monthly_increase * annual_minimum
    monthly_out = monthly_increase + monthly_increase
    result = monthly_out
    return result

print(solution())