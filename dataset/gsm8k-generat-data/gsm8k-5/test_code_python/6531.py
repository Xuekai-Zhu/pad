def solution():
    starting_logs = 6  # The cookfire was built with six logs
    logs_per_hour = 3  # The cookfire burns three logs every hour
    logs_added_per_hour = 2  # Two more logs are added to the cookfire at the end of every hour
    hours = 3  # The cookfire burns for three hours

    # Calculate the total number of logs burned over three hours
    total_logs_burned = logs_per_hour * hours

    # Calculate the total number of logs added over three hours
    total_logs_added = logs_added_per_hour * (hours - 1)  # Only two logs are added during the final hour

    # Calculate the total number of logs remaining after three hours
    logs_remaining = starting_logs + total_logs_added - total_logs_burned
    result = logs_remaining
    return result

print(solution())