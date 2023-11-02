def solution():
    taxable_income = 100000 - 30000  # taxable income after deductions
    taxes_on_first_20000 = 20000 * 0.1  # taxes on the first $20,000 at 10%
    taxes_on_rest = (taxable_income - 20000) * 0.2  # taxes on the rest at 20%
    total_taxes = taxes_on_first_20000 + taxes_on_rest
    result = total_taxes
    return result

print(solution())