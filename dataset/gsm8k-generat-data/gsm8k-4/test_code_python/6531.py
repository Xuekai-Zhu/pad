def solution():
    """A cookfire burns three logs every hour. It was built with six logs to start. If it gets two more logs added to it at the end of every hour, how many logs will be left after 3 hours?"""
    # Define the number of logs at the start
    logs = 6

    # Burn three logs every hour for three hours
    logs -= 3*3

    # Add two logs at the end of every hour for three hours
    logs += 2*3

    # return the result
    result = logs
    return result

print(solution())