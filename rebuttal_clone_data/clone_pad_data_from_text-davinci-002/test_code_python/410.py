def solution():
    record = 54000
    jumps_per_second = 3
    seconds_per_minute = 60
    minutes_per_hour = 60
    total_jumps = record * jumps_per_second
    total_hours = total_jumps / (seconds_per_minute * minutes_per_hour)
    result = total_hours
    return result

print(solution())