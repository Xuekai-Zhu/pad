def solution():
    # Define Brendan's hourly wage and tips
    wage = 6
    tips = 12

    # Calculate Brendan's total income for the week
    total_income = (wage * 8 * 2) + (wage * 12) + (tips * 8 * 2) + (tips * 12)

    # Calculate Brendan's reported tips for the week
    reported_tips = (tips * 8 * 2) + (tips * 12) / 3

    # Calculate Brendan's taxable income for the week
    taxable_income = total_income - reported_tips

    # Calculate Brendan's tax payment for the week
    tax_payment = taxable_income * 0.2

    result = tax_payment
    return result

print(solution())