def solution():
    # Calculate taxes paid before the tax rate increase
    before_tax_rate = 0.20
    before_income = 1000000
    before_taxes = before_income * before_tax_rate

    # Calculate taxes paid after the tax rate increase
    after_tax_rate = 0.30
    after_income = 1500000
    after_taxes = after_income * after_tax_rate

    # Calculate the difference in taxes paid
    tax_increase = after_taxes - before_taxes
    result = tax_increase
    return result

print(solution())