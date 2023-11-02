def solution():
    
    income = 100000
    deductions = 30000
    taxable_income = income - deductions
    first_tier = min(taxable_income, 20000)
    second_tier = max(0, taxable_income - 20000)
    tax = (first_tier * 0.1) + (second_tier * 0.2)
    result = tax
    return result

print(solution())