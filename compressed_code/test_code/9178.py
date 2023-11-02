def solution():
    
    normal_work_hours = 10
    extra_hours = 5
    total_work_hours_per_day = normal_work_hours + extra_hours
    total_project_hours = 1500
    total_work_days = total_project_hours / total_work_hours_per_day
    result = total_work_days
    return result

print(solution())