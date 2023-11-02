def solution():
    
    work_hours_per_day = 8
    work_hours_per_chair = 5
    total_days = 10
    total_work_hours = work_hours_per_day * total_days
    chairs_per_work_hour = 1 / work_hours_per_chair
    total_chairs = total_work_hours * chairs_per_work_hour
    result = total_chairs
    return result

print(solution())