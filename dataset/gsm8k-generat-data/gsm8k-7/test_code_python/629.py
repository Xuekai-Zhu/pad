def solution():
    num_periods_per_day = 5
    num_days_per_month = 24
    pay_per_period = 5
    num_months_worked = 6

    # Calculate the total number of periods taught in a month
    total_periods = num_periods_per_day * num_days_per_month

    # Calculate the total pay per month
    total_pay_per_month = total_periods * pay_per_period

    # Calculate the total pay for 6 months
    total_pay = total_pay_per_month * num_months_worked
    result = total_pay
    return result

print(solution())