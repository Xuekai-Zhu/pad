def solution():
    wage_per_hour = 6  # Brendan makes $6/hour as a waiter
    tip_per_hour = 12  # Brendan makes an average of $12 in tips each hour
    num_shifts_8_hours = 2  # Brendan has 2 8-hour shifts this week
    num_shifts_12_hours = 1  # Brendan has 1 12-hour shift this week
    reported_tip_percentage = 1 / 3  # Brendan only reports 1/3 of his tips to the IRS
    tax_percentage = 0.2  # Brendan is supposed to pay 20% of his income in taxes

    # Calculate the total wage Brendan earns from his shifts
    total_wage = (wage_per_hour * 8 * num_shifts_8_hours) + (wage_per_hour * 12 * num_shifts_12_hours)

    # Calculate the total tips Brendan earns from his shifts
    total_tips = (tip_per_hour * 8 * num_shifts_8_hours) + (tip_per_hour * 12 * num_shifts_12_hours)

    # Calculate the total income before taxes
    income_before_taxes = total_wage + total_tips

    # Calculate the taxable income
    taxable_income = income_before_taxes - (total_tips * reported_tip_percentage)

    # Calculate the taxes Brendan owes
    taxes_owed = taxable_income * tax_percentage

    result = taxes_owed
    return result

print(solution())