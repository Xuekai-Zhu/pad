def solution():
    # Calculate the tax paid before the rate change
    previous_tax = 0.2 * 1000000

    # Calculate the tax paid after the rate change
    current_tax = 0.3 * 1500000

    # Calculate the difference in taxes
    tax_difference = current_tax - previous_tax

    result = tax_difference
    return result

print(solution())