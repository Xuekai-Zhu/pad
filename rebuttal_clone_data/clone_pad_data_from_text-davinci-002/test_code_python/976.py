def solution():
    daily_salary = 10
    days_worked_per_week = 7
    hours_worked_per_day = 8
    hours_worked_on_weekends = 4
    total_hours_worked =  hours_worked_per_day * days_worked_per_week + hours_worked_on_weekends
    weekly_salary = total_hours_worked * daily_salary
    result = weekly_salary
    return result

print(solution())