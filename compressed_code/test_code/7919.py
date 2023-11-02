def solution():
    
    income = 100000
    deductions = 30000
    taxable_income = income - deductions
    tax_10_percent = min(taxable_income, 20000) * 0.1
    tax_20_percent = max(taxable_income - 20000, 0) * 0.2
    total_tax = tax_10_percent + tax_20_percent
    result = total_tax
    return result

print(solution())