def solution():
    
    monthly_salary = 5000
    tax_rate = 0.1
    after_tax_salary = monthly_salary * (1 - tax_rate)
    rent_payment = (after_tax_salary * 3/5) / 2
    result = rent_payment
    return result

print(solution())