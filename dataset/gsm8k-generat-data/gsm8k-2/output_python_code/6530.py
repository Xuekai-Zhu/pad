def solution():
    """A cookfire burns three logs every hour. It was built with six logs to start. If it gets two more logs added to it at the end of every hour, how many logs will be left after 3 hours?"""
    starting_logs = 6
    burned_logs = 3 * 3
    added_logs = 2 * 3
    remaining_logs = starting_logs + added_logs - burned_logs
    result = remaining_logs
    return result

print(solution())