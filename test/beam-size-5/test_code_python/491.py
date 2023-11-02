def solution():
    
    work_hours_per_day = 8
    walk_time_per_hour = 5
    days = 5
    total_work_hours = work_hours_per_day * days
    total_walk_time = total_work_hours * walk_time_per_hour
    result = total_walk_time
    return result

print(solution())