def solution():
    # Calculate Ben's after-tax income
    tax_rate = 1/3
    after_tax_income = 400 / 0.2

    # Calculate Ben's pre-tax income
    pre_tax_income = after_tax_income / (1 - tax_rate)
    result = pre_tax_income
    return result

print(solution())