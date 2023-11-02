def solution():
    # Define initial log count and log usage per hour
    total_logs = 6
    logs_per_hour = 3

    # Calculate log count after each hour and add 2 logs
    for i in range(3):
        total_logs -= logs_per_hour
        total_logs += 2
    
    result = total_logs
    return result

print(solution())