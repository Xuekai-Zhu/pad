def solution():
    
    salary = 40000
    tax_percentage = 0.2
    healthcare_percentage = 0.1
    union_dues = 800
    remaining_salary = salary - (salary * tax_percentage) - (salary * healthcare_percentage) - union_dues
    result = remaining_salary
    return result

print(solution())