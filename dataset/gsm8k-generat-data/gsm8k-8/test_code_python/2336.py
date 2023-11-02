def solution():
    tv_cost = 1700
    weekly_hours = 30
    hourly_wage = 10
    weekly_pay = weekly_hours * hourly_wage
    weeks_to_save = tv_cost // weekly_pay + 1
    extra_hours = (weeks_to_save * weekly_hours) - (tv_cost // hourly_wage)
    result = extra_hours
    return result

print(solution())