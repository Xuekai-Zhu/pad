def solution():
    num_employees = 500
    hourly_rate = 12
    hours_per_day = 10
    days_per_week = 5
    weeks_per_month = 4

    # Calculate the total monthly payroll before the new hires
    payroll_before = num_employees * hourly_rate * hours_per_day * days_per_week * weeks_per_month

    # Calculate the total monthly payroll after the new hires
    num_employees += 200
    payroll_after = num_employees * hourly_rate * hours_per_day * days_per_week * weeks_per_month

    # Calculate the difference in payroll after the new hires
    increase_in_payroll = payroll_after - payroll_before
    result = increase_in_payroll
    return result

print(solution())