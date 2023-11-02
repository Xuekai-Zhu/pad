def solution():
    monthly_salary = 5000
    tax_rate = 10
    rent_expense = monthly_salary * 3/5
    after_tax_salary = monthly_salary - (monthly_salary*tax_rate/100)
    monthly_rent = after_tax_salary/5
    result = monthly_rent
    return result

print(solution())