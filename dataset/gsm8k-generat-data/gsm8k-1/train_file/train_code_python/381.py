def solution():
    """It takes David 10 minutes to wash 4 windows. David's house has 64 windows. How many minutes will it take David to wash all of the windows?"""
    windows_per_cycle = 4
    time_per_cycle = 10
    total_windows = 64
    cycles_needed = total_windows / windows_per_cycle
    time_needed = cycles_needed * time_per_cycle
    result = time_needed
    return result

print(solution())