def solution():
    old_ hourly_rate = 40
    new_hourly_rate = old_hourly_rate * 1.05
    hours_worked = 8
    days_worked = 5
    weekly_bill = 600
    new_bill = weekly_bill + 100
    old_weekly_paycheck = old_hourly_rate * hours_worked * days_worked
    new_weekly_paycheck = new_hourly_rate * hours_worked * days_worked
    old_leftover = old_weekly_paycheck - weekly_bill
    new_leftover = new_weekly_paycheck - new_bill
    result = new_leftover - old_leftover
    return result

print(solution())