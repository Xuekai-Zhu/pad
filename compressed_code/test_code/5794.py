def solution():
    
    work_days_per_week = 5
    work_distance = 20
    weekend_ride_distance = 200
    speed = 25
    time_work = (2 * work_distance * work_days_per_week) / speed
    time_weekend = weekend_ride_distance / speed
    total_time = time_work + time_weekend
    result = total_time
    return result

print(solution())