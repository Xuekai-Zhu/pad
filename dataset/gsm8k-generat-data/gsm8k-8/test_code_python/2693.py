def solution():
    # Calculate taxable income
    taxable_income = 100000 - 30000

    # Calculate tax on the first $20,000
    tax_20k = 0.1 * 20000

    # Calculate tax on the rest of the income
    rest_income = taxable_income - 20000
    tax_rest = 0.2 * rest_income

    # Calculate total tax liability
    total_tax = tax_20k + tax_rest
    result = total_tax
    return result

print(solution())