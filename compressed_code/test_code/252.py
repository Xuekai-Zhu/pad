def solution():
    
    daily_salary = 40
    tax_percentage = 0.1
    salary_after_tax = daily_salary * (1 - tax_percentage)
    total_salary = salary_after_tax * 30
    result = total_salary
    return result

print(solution())