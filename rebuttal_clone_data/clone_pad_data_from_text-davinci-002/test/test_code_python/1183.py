def solution():
    monthly_salary = 2000
    tax_percentage = 20
    insurance_percentage = 5
    utility_percentage = 25
    tax_deduction = monthly_salary * (tax_percentage / 100)
    insurance_deduction = monthly_salary * (insurance_percentage / 100)
    monthly_salary_after_deductions = monthly_salary - tax_deduction - insurance_deduction
    utility_bill = monthly_salary_after_deductions * (utility_percentage / 100)
    monthly_salary_after_utility_bill = monthly_salary_after_deductions - utility_bill
    result = monthly_salary_after_utility_bill
    
    return result

print(solution())