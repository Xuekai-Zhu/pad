def solution():
    Terry_daily_income = 24
    Jordan_daily_income = 30
    days_in_week = 7
    Terry_weekly_income = Terry_daily_income * days_in_week
    Jordan_weekly_income = Jordan_daily_income * days_in_week
    income_difference = Jordan_weekly_income - Terry_weekly_income
    result = income_difference
    return result

print(solution())