def solution():
    hourly_wage = 6
    hours_worked = [8, 8, 12]
    tips_per_hour = 12
    reported_tips = tips_per_hour / 3
    total_tips = reported_tips * len(hours_worked)
    total_income = hourly_wage * sum(hours_worked) + total_tips
    tax_rate = 20
    taxes_owed = (total_income * tax_rate) / 100
    result = taxes_owed
    return result

print(solution())