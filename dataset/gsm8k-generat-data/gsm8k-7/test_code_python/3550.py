def solution():
    daily_pay = 8
    days_per_week = 5
    extra_day_pay = daily_pay * 1.5
    extra_day = 1

    # Calculate the total pay per week without overtime
    weekly_pay = daily_pay * days_per_week

    # Calculate the total pay per week with overtime
    weekly_pay_overtime = weekly_pay + (extra_day_pay * extra_day)

    # Calculate the total pay after a month with overtime
    monthly_pay_overtime = weekly_pay_overtime * 4
    result = monthly_pay_overtime
    return result

print(solution())