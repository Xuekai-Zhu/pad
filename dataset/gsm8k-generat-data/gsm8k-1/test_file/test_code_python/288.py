def solution():
    """Susan earns $5 every 10 minutes for an online task she does. If she works between 8 a.m. and 11 a.m. and pauses in between for half an hour, how much money does she earn for the online task?"""
    work_time = 3*60 - 30 # in minutes
    earn_rate = 5/10 # dollars per minute
    earnings = work_time * earn_rate
    result = earnings
    return result

print(solution())