def solution():
    sick_days_allotment = 10
    vacation_days_allotment = 10
    workday_hours = 8

    # Calculate the number of sick days Mark used
    sick_days_used = sick_days_allotment / 2

    # Calculate the number of vacation days Mark used
    vacation_days_used = vacation_days_allotment / 2

    # Calculate the total number of hours' worth of days Mark used
    total_days_used = (sick_days_used + vacation_days_used) * workday_hours

    # Calculate the total number of hours' worth of days Mark has left
    total_days_left = ((sick_days_allotment + vacation_days_allotment) / 2 - (sick_days_used + vacation_days_used)) * workday_hours
    result = total_days_left
    return result

print(solution())