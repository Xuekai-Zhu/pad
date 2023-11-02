def solution():
    normal_work_hours = 10
    extra_work_hours = 5
    total_work_hours = normal_work_hours + extra_work_hours
    total_project_hours = 1500
    hours_per_day = total_work_hours
    
    num_days = total_project_hours / hours_per_day
    
    result = num_days
    return result

print(solution())