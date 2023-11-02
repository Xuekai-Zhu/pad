def solution():
    """John has to pay taxes. He earned $100,000 for the year. He has $30,000 in deductions. The first $20,000 of taxable income is taxed at 10%. The rest is taxed at 20%. How much does he pay in taxes?"""
    income = 100000
    deductions = 30000
    taxable_income = income - deductions
    tax_10_percent = min(taxable_income, 20000) * 0.1
    tax_20_percent = max(taxable_income - 20000, 0) * 0.2
    total_tax = tax_10_percent + tax_20_percent
    result = total_tax
    return result

print(solution())