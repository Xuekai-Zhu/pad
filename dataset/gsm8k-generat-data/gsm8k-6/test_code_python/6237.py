def solution():
    # Calculate Brendan's income before taxes and tips
    income_before_tips = (6 * 8 * 2) + (6 * 12)  # Brendan works 2 8-hour shifts and 1 12-hour shift
    # Calculate Brendan's tips before taxes
    tips = 12 * (8 * 2 + 12)  # Brendan makes $12 in tips each hour and works 2 8-hour shifts and 1 12-hour shift
    # Calculate Brendan's total income with tips
    total_income = income_before_tips + tips
    # Calculate Brendan's taxable income
    taxable_income = total_income - (tips/3)  # Brendan only reports 1/3 of his tips to the IRS
    # Calculate Brendan's taxes
    taxes = 0.2 * taxable_income  # Brendan is supposed to pay 20% of his income in taxes
    result = taxes
    return result

print(solution())