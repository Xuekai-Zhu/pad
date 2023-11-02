def solution():
    """A company has 500 employees, each paid $12 per hour, working 10 hours a day, five days a week, 4 weeks a month. In August, the amount of work increased, and the company hired 200 more people. How much money does the company pay in total per month after the new hires?"""
    hourly_rate = 12
    work_hours_per_day = 10
    work_days_per_week = 5
    work_weeks_per_month = 4
    initial_employee_count = 500
    new_employee_count = 200
    total_employee_count = initial_employee_count + new_employee_count
    total_working_hours_per_day = work_hours_per_day * total_employee_count
    total_working_hours_per_week = total_working_hours_per_day * work_days_per_week
    total_working_hours_per_month = total_working_hours_per_week * work_weeks_per_month
    total_pay_per_month = total_working_hours_per_month * hourly_rate
    result = total_pay_per_month
    return result

print(solution())