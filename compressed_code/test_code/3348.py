def solution():
    
    normal_work_hours = 10
    extra_hours = 5
    total_hours_per_day = normal_work_hours + extra_hours
    total_project_hours = 1500
    days_to_complete = total_project_hours / total_hours_per_day
    result = days_to_complete
    return result

print(solution())