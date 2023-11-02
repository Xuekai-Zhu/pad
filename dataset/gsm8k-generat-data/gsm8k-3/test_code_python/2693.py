def solution():
    """John has to pay taxes.  He earned $100,000 for the year.  He has $30,000 in deductions.  The first $20,000 of taxable income is taxed at 10%.  The rest is taxed at 20%.  How much does he pay in taxes?"""
    # Calculate taxable income
    income = 100000
    deductions = 30000
    taxable_income = income - deductions

    # Calculate tax
    if taxable_income > 20000:
        tax = 20000 * 0.1 + (taxable_income - 20000) * 0.2
    else:
        tax = taxable_income * 0.1

    # Display tax
    result = tax
    return result

print(solution())