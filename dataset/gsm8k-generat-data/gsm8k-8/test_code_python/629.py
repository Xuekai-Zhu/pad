def solution():
    # Define the variables
    periods_per_day = 5
    work_days_per_month = 24
    pay_per_period = 5
    months_worked = 6

    # Calculate the total number of periods taught
    total_periods = periods_per_day * work_days_per_month * months_worked

    # Calculate the total pay earned
    total_pay = total_periods * pay_per_period
    result = total_pay
    return result

print(solution())