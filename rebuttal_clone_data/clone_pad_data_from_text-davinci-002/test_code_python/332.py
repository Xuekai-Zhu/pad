def solution():
    salary = 60000
    tax_rate = 18
    taxes_owed = salary * (tax_rate / 100)
    salary_after_taxes = salary - taxes_owed
    result = salary_after_taxes
    return result

print(solution())