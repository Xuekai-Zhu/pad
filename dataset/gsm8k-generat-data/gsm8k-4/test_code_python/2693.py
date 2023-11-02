def solution():
    """John has to pay taxes.  He earned $100,000 for the year.  He has $30,000 in deductions.  The first $20,000 of taxable income is taxed at 10%.  The rest is taxed at 20%.  How much does he pay in taxes?"""
    # Define the income and deductions
    income = 100000
    deductions = 30000

    # Calculate the taxable income
    taxable_income = income - deductions

    # Calculate the tax on the first $20,000 of taxable income
    first_tax = min(taxable_income, 20000) * 0.1

    # Calculate the tax on the rest of the taxable income
    rest_tax = max(taxable_income - 20000, 0) * 0.2

    # Calculate the total tax
    total_tax = first_tax + rest_tax

    # return the result
    result = total_tax
    return result

print(solution())