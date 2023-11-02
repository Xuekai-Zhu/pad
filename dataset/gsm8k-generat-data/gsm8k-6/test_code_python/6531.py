def solution():
    # Calculate the total number of logs added in 3 hours
    added_logs = 2 * 3  # 2 logs added per hour for 3 hours
    remaining_logs = (6 + added_logs) - (3 * 3)  # 6 logs to start, 3 logs burned per hour for 3 hours
    result = remaining_logs
    return result

print(solution())