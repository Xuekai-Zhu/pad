def solution():
    
    old_salary = 1000000
    new_salary = 1500000
    old_tax = old_salary * 0.2
    new_tax = new_salary * 0.3
    tax_increase = new_tax - old_tax
    result = tax_increase
    return result

print(solution())