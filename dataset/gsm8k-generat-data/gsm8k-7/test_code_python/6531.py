def solution():
    initial_logs = 6
    logs_burned_per_hour = 3
    logs_added_per_hour = 2
    hours = 3

    # Calculate the total number of logs burned
    total_logs_burned = logs_burned_per_hour * hours

    # Calculate the total number of logs added
    total_logs_added = logs_added_per_hour * (hours - 1)  # One log was already added at the start

    # Calculate the final number of logs
    final_logs = initial_logs + total_logs_added - total_logs_burned
    result = final_logs
    return result

print(solution())