def solution():
    """John has to pay taxes. He earned $100,000 for the year. He has $30,000 in deductions. The first $20,000 of taxable income is taxed at 10%. The rest is taxed at 20%. How much does he pay in taxes?"""
    income = 100000
    deductions = 30000
    taxable_income = income - deductions
    first_tier = min(taxable_income, 20000)
    second_tier = max(0, taxable_income - 20000)
    tax = (first_tier * 0.1) + (second_tier * 0.2)
    result = tax
    return result

print(solution())