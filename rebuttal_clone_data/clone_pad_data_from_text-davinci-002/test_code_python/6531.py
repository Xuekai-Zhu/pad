def solution():
    logs_burned_per_hour = 3
    total_hours = 3
    logs_added_per_hour = 2
    total_logs = 6 + (total_hours * logs_added_per_hour) - (total_hours * logs_burned_per_hour)
    result = total_logs
    return result

print(solution())