def solution():
    
    seconds_per_minute = 60
    minutes_per_hour = 60
    total_seconds = seconds_per_minute * minutes_per_hour
    instances_per_second = 1 / 5
    total_instances = total_seconds * instances_per_second
    result = total_instances
    return result

print(solution())