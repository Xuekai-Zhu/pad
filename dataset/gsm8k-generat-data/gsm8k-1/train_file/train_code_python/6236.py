def solution():
    """Brendan makes $6/hour as a waiter. He's scheduled for 2 8-hour shifts and 1 12-hour shift this week. He also makes an average of $12 in tips each hour. Brendan is supposed to pay 20% of his income in taxes, but he only reports 1/3rd of his tips to the IRS. How much money does Brendan pay in taxes each week?"""
    hourly_wage = 6
    num_shifts = 3
    hours_per_shift = [8, 8, 12]
    total_hours = sum(hours_per_shift)
    tips_per_hour = 12
    total_tips = total_hours * tips_per_hour
    taxable_income = (total_hours * hourly_wage) + (total_tips / 3)
    tax_rate = 0.2
    taxes_owed = taxable_income * tax_rate
    result = taxes_owed
    return result

print(solution())