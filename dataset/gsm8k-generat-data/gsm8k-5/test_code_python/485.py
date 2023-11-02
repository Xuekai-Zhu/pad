def solution():
    hours_per_day = 35 / 5  # Lance works 35 hours a week, spread equally over 5 workdays
    hourly_pay = 9  # Lance earns $9 an hour

    # Calculate Lance's daily earnings
    daily_pay = hours_per_day * hourly_pay
    result = daily_pay
    return result

print(solution())