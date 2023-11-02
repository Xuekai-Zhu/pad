def solution():
    """Every day Janet spends 8 minutes looking for her keys and another 3 minutes complaining after she finds them. If Janet stops losing her keys, how many minutes will she save every week?"""
    # Calculate the total time Janet spends searching and complaining each day
    total_time_daily = 8 + 3

    # Calculate the total time Janet will save per week
    total_time_saved_weekly = total_time_daily * 7

    # return the result
    result = total_time_saved_weekly
    return result

print(solution())