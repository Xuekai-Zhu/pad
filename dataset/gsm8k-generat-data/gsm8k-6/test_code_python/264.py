def solution():
    weekdays = 5  # number of weekdays in a week
    weekend_days = 2  # number of weekend days in a week
    weekday_income = 600  # income earned on weekdays
    weekend_income = 2 * weekday_income  # income earned on weekend days
    days_in_month = 30  # assuming 30 days in a month

    total_income = (weekdays * weekday_income + weekend_days * weekend_income) * days_in_month
    result = total_income
    return result

print(solution())