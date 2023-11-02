def solution():
    """Mark plants a beanstalk below his second-story window, which is 20 feet off the ground. The beanstalk doubles its height every day. If the beanstalk starts out 4 feet tall, how many days will it take to be taller than Mark's window?"""
    current_height = 4
    window_height = 20
    days = 0
    while current_height <= window_height:
        current_height *= 2
        days += 1
    result = days
    return result

print(solution())