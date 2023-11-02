def solution():
    """It takes David 10 minutes to wash 4 windows. David's house has 64 windows. How many minutes will it take David to wash all of the windows?"""
    windows_per_minute = 4/10
    total_windows = 64
    washing_time = total_windows / windows_per_minute
    result = washing_time
    return result

print(solution())