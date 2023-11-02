def solution():
    old_tax_rate = 20
    new_tax_rate = 30
    old_salary = 1000000
    new_salary = 1500000
    old_taxes_paid = old_salary * (old_tax_rate / 100)
    new_taxes_paid = new_salary * (new_tax_rate / 100)
    taxes_increase = new_taxes_paid - old_taxes_paid
    result = taxes_increase
    return result

print(solution())