def solution():
    days_of_the_week = ['Sunday', 'Tuesday', 'Thursday']
    weekends = ['Saturday', 'Sunday']
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    speed_walking = 2
    speed_running = 10
    distance_to_store = 4
    time_walking = distance_to_store / speed_walking
    time_running = distance_to_store / speed_running
    total_time = 0
    
    for day in days_of_the_week:
        if day in weekends:
            total_time += time_walking
        elif day in weekdays:
            total_time += time_running
    
    average_time = total_time / len(days_of_the_week)
    
    return average_time

print(solution())