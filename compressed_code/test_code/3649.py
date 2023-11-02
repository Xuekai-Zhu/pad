def solution():
    
    
    walking_distance = 3
    walking_speed = 3
    walking_time = walking_distance / walking_speed

    
    running_distance = 10
    running_speed = 5
    running_time = running_distance / running_speed

    
    total_time = walking_time + running_time

    
    days_per_week = 7
    total_weekly_time = total_time * days_per_week

    result = total_weekly_time
    return result

print(solution())