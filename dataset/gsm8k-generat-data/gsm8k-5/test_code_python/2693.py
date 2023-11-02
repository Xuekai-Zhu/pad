def solution():
    income = 100000  # John earned $100,000 for the year
    deductions = 30000  # John has $30,000 in deductions
    taxable_income = income - deductions  # John's taxable income

    # Calculate the tax on the first $20,000 of taxable income
    tax_on_first = 0.1 * min(20000, taxable_income)

    # Calculate the tax on the remaining taxable income
    remaining_taxable_income = max(0, taxable_income - 20000)
    tax_on_remaining = 0.2 * remaining_taxable_income

    # Calculate the total tax John has to pay
    total_tax = tax_on_first + tax_on_remaining
    result = total_tax
    return result

print(solution())