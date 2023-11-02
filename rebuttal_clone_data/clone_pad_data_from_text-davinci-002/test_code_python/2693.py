def solution():
    earned = 100000
    deductions = 30000
    first_tax bracket = 20000
    tax_rate_1 = 10
    tax_rate_2 = 20
    taxable_income = earned - deductions
    tax_amount_1 = first_tax_bracket * (tax_rate_1 / 100)
    tax_amount_2 = (taxable_income - first_tax_bracket) * (tax_rate_2 / 100)
    total_taxes = tax_amount_1 + tax_amount_2
    result = total_taxes
    return result

print(solution())