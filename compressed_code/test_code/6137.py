def solution():
    
    sick_days_allotted = 10
    vacation_days_allotted = 10
    days_used = (sick_days_allotted + vacation_days_allotted) / 2
    hours_left = (sick_days_allotted + vacation_days_allotted - days_used) * 8
    result = hours_left
    return result

print(solution())