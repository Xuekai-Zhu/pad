def solution():
    
    total_jumps = 54000
    jumps_per_second = 3
    seconds_per_hour = 3600
    total_hours = total_jumps / jumps_per_second / seconds_per_hour
    result = total_hours
    return result

print(solution())