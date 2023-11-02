def solution():
    old_hourly_pay = 16
    old_hours_per_week = 25
    new_hourly_pay = 20
    new_hours_per_week = 40
    weeks_per_year = 52

    # Calculate the annual income from the old job
    old_weekly_income = old_hourly_pay * old_hours_per_week
    old_annual_income = old_weekly_income * weeks_per_year

    # Calculate the annual income from the new job
    new_weekly_income = new_hourly_pay * new_hours_per_week
    new_annual_income = new_weekly_income * weeks_per_year

    # Calculate the difference in annual income between the two jobs
    income_difference = new_annual_income - old_annual_income
    result = income_difference
    return result

print(solution())