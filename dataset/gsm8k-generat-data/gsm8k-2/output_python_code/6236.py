def solution():
    """Brendan makes $6/hour as a waiter. He's scheduled for 2 8-hour shifts and 1 12-hour shift this week. He also makes an average of $12 in tips each hour. Brendan is supposed to pay 20% of his income in taxes, but he only reports 1/3rd of his tips to the IRS. How much money does Brendan pay in taxes each week?"""
    hourly_wage = 6
    tips_per_hour = 12
    hours_per_week = (2 * 8) + 12
    total_tip_income = tips_per_hour * hours_per_week
    reported_tip_income = total_tip_income / 3
    total_income = (hourly_wage * hours_per_week) + total_tip_income
    taxable_income = total_income * 0.8  # after deducting reported tips
    taxes = taxable_income * 0.2
    result = taxes
    return result

print(solution())