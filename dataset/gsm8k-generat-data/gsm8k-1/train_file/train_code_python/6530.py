def solution():
    """A cookfire burns three logs every hour. It was built with six logs to start. If it gets two more logs added to it at the end of every hour, how many logs will be left after 3 hours?"""
    starting_logs = 6
    logs_burned_per_hour = 3
    logs_added_per_hour = 2
    total_logs = starting_logs + (logs_added_per_hour * 3) - (logs_burned_per_hour * 3)
    result = total_logs
    return result

print(solution())