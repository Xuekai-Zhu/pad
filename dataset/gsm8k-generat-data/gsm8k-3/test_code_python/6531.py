def solution():
    """A cookfire burns three logs every hour. It was built with six logs to start. If it gets two more logs added to it at the end of every hour, how many logs will be left after 3 hours?"""
    # Define the starting logs and logs added per hour
    start_logs = 6
    add_logs = 2
    burn_logs = 3

    # Calculate the total logs after 3 hours
    total_logs = start_logs + (add_logs * 3) - (burn_logs * 3)

    # Display the total logs remaining after 3 hours
    result = total_logs
    return result

print(solution())