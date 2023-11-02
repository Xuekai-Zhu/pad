def solution():
    sick_days_per_year = 10
    vacation_days_per_year = 10
    hours_in_a_day = 8
    total_hours_sick = sick_days_per_year * hours_in_a_day / 2
    total_hours_vacation = vacation_days_per_year * hours_in_a_day / 2
    total_hours_left = (sick_days_per_year * hours_in_a_day) + (vacation_days_per_year * hours_in_a_day) - (total_hours_sick + total_hours_vacation)
    result = total_hours_left
    return result

print(solution())