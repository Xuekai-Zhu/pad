def solution():
    # Calculate the amount of taxes paid before the tax rate increase
    before_tax = 0.2 * 1000000

    # Calculate the amount of taxes paid after the tax rate increase
    after_tax = 0.3 * 1500000

    # Calculate the difference in taxes paid
    tax_difference = after_tax - before_tax
    result = tax_difference
    return result

print(solution())