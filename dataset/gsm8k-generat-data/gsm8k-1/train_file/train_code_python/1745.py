def solution():
    """A company has 500 employees, each paid $12 per hour, working 10 hours a day, five days a week, 4 weeks a month. In August, the amount of work increased, and the company hired 200 more people. How much money does the company pay in total per month after the new hires?"""
    num_employees = 500 + 200
    wage_per_hour = 12
    hours_per_day = 10
    days_per_week = 5
    weeks_per_month = 4
    total_hours_per_month = num_employees * hours_per_day * days_per_week * weeks_per_month
    total_pay_per_month = total_hours_per_month * wage_per_hour
    result = total_pay_per_month
    return result

print(solution())