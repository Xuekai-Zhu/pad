def solution():
    income = 100000
    deductions = 30000
    taxable_income = income - deductions

    # Calculate the tax on the first $20,000 of taxable income
    first_tax = min(taxable_income, 20000) * 0.1

    # Calculate the tax on the rest of the taxable income
    second_tax = max(0, taxable_income - 20000) * 0.2

    # Calculate the total tax that John has to pay
    total_tax = first_tax + second_tax
    result = total_tax
    return result

print(solution())