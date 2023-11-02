def solution():
    hourly_wage = 18.00  # hourly wage of Tina
    daily_hours = 10  # number of hours Tina works every day
    overtime_hours = daily_hours - 8  # number of hours Tina works overtime every day
    overtime_pay = (hourly_wage * 1.5) * overtime_hours  # overtime pay of Tina
    daily_pay = hourly_wage * 8 + overtime_pay  # daily pay of Tina
    weekly_pay = daily_pay * 5  # weekly pay of Tina
    result = weekly_pay
    return result

print(solution())