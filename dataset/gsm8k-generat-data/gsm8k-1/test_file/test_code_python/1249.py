def solution():
    """Tim spends 6 hours each day at work answering phones. It takes him 15 minutes to deal with a call. How many calls does he deal with during his 5 day work week?"""
    hours_per_day = 6
    minutes_per_call = 15
    calls_per_day = (hours_per_day * 60)/minutes_per_call
    work_days_per_week = 5
    total_calls = calls_per_day * work_days_per_week
    result = total_calls
    return result

print(solution())